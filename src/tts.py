import pyttsx3


def speak(text: str) -> None:
    """
    تحول النص لصوت مسموع.

    input:  نص (string) — جواب Jake
    output: لا شي — يشغل الصوت مباشرة
    """

    # pyttsx3.init() = يشغل محرك الصوت المحلي على جهازك
    # مو محتاج إنترنت — يشتغل offline كامل
    engine = pyttsx3.init()

    # نجيب كل الأصوات المتاحة على الجهاز
    voices = engine.getProperty('voices')

    # ندور على أول صوت إنجليزي ونختاره
    # ليش؟ الافتراضي ممكن يكون صوت عربي أو لغة ثانية
    for voice in voices:
        if "english" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    # نضبط السرعة — الافتراضي 200 (سريع شوية)
    # 150 = أطبيعي وأوضح للاستماع
    engine.setProperty('rate', 150)

    # say()        = يحضر النص للقراءة
    # runAndWait() = يشغل الصوت وينتظر لحين يخلص
    # ليش runAndWait؟ بدونها يكمل الكود قبل ما يخلص الكلام
    engine.say(text)
    engine.runAndWait()