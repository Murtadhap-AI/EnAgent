import ollama
import re
import json  
from src.stt import listen
from src.tts import speak
from src.prompts import JAKE_SYSTEM_PROMPT
from src.memory import load_memory, save_memory, update_mistakes, update_topics


def think(user_message: str, conversation_history: list, memory: dict):
    """
    Jake يفكر ويرد — مع streaming جملة جملة.

    input:  نص المستخدم + تاريخ المحادثة + الذاكرة
    output: الرد الكامل (للذاكرة) + تاريخ محدّث
    """

    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    memory_context = ""
    if memory["mistakes"]:
        errors = ", ".join([m["error"] for m in memory["mistakes"]])
        memory_context = f"\n\nUser's recurring mistakes to watch for: {errors}"
    if memory["topics_covered"]:
        topics = ", ".join(memory["topics_covered"])
        memory_context += f"\nTopics already covered: {topics}"

    
    response = ollama.chat(
        model="qwen3:1.7b",
        messages=[
            {"role": "system", "content": JAKE_SYSTEM_PROMPT + memory_context},
            *conversation_history
        ],
        stream=True  
    )

    full_reply = ""   
    buffer = ""       

    for chunk in response:
        piece = chunk['message']['content']

        full_reply += piece   # 
        buffer += piece       #

        if any(punct in buffer for punct in [".", "!", "?"]):
            sentence = buffer.strip()
            if sentence:
                speak(sentence)   # ← نحجي الجملة فوراً بدون انتظار
            buffer = ""           # نفضّي الـ buffer للجملة الجاية

    if buffer.strip():
        speak(buffer.strip())

    conversation_history.append({
        "role": "assistant",
        "content": full_reply
    })

    return full_reply, conversation_history

def parse_jake_reply(full_reply: str) -> tuple[str, dict]:
    """
    تفصل كلام Jake عن بيانات الذاكرة.

    input:  الرد الكامل من Jake (فيه [MEMORY] block بالنهاية)
    output: (الكلام النظيف, بيانات الذاكرة كـ dict)

    مثال:
    input:  "Ha yeah! We say 'went' bro!\n\n[MEMORY]\n{...}\n[/MEMORY]"
    output: ("Ha yeah! We say 'went' bro!",
             {"mistakes": [{"error": "go", "correction": "went"}], "topic": "past tense"})
    """

    
    pattern = r'\[MEMORY\](.*?)\[/MEMORY\]'
    match = re.search(pattern, full_reply, re.DOTALL)

    if not match:
        
        return full_reply.strip(), {}

   
    memory_json = match.group(1).strip()

    
    clean_reply = full_reply[:match.start()].strip()

    try:
        
        memory_data = json.loads(memory_json)
    except json.JSONDecodeError:
        
        memory_data = {}

    return clean_reply, memory_data


def extract_and_update(memory: dict, memory_data: dict) -> dict:
    """
    تحدّث الذاكرة بالأخطاء والمواضيع الجديدة.

    input:  الذاكرة الحالية + بيانات جديدة من parse_jake_reply
    output: الذاكرة بعد التحديث
    """

    # نعالج كل خطأ وصلنا من Jake
    for mistake in memory_data.get("mistakes", []):
        error = mistake.get("error", "")
        correction = mistake.get("correction", "")
        # نتأكد الاثنين موجودين قبل ما نحفظ
        if error and correction:
            memory = update_mistakes(memory, error, correction)

    # نعالج الموضوع — topic وحيد لكل رد
    topic = memory_data.get("topic", "")
    if topic:
        memory = update_topics(memory, topic)

    return memory


def main():
    print("🎯 Jake is ready! Start speaking in English.")
    print("Say 'bye' or 'exit' to stop.\n")

   
    memory = load_memory()
    memory["sessions"] += 1
    print(f"📚 Session #{memory['sessions']} — Welcome back!")

    if memory["mistakes"]:
        print(f"⚠️  Jake remembers your mistakes: {[m['error'] for m in memory['mistakes']]}\n")

    # قائمة فارغة — تتملأ بكل رسالة في الجلسة
    conversation_history = []

    while True:
        
        user_input = listen()

        if user_input is None:
            continue  # نرجع للبداية ونسمع مرة ثانية

        if user_input.lower() in ["bye", "exit", "goodbye"]:
            save_memory(memory)
            print("💾 Memory saved!")
            speak("Alright man, catch you later! Keep practicing!")
            break

        # Jake يفكر ويرد (الرد الكامل فيه [MEMORY] block)
        jake_reply, conversation_history = think(user_input, conversation_history, memory)

        #  نفصل كلام Jake عن بيانات الذاكرة
        clean_reply, memory_data = parse_jake_reply(jake_reply)

        #  نطبع الكلام النظيف بس — بدون [MEMORY]
        print(f"Jake: {clean_reply}\n")

        #  نحدّث الذاكرة بالبيانات الجديدة
        memory = extract_and_update(memory, memory_data)

        #  Jake يحجي — بدون [MEMORY] block
        speak(clean_reply)


if __name__ == "__main__":
    main()