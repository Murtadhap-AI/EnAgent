import speech_recognition as sr


def listen() -> str | None:
    """
    تسمع صوت المستخدم وتحوله لنص.

    input:  لا شي — تفتح المايك مباشرة
    output: نص (string) لو نجح، None لو فشل
    """

    # sr.Recognizer() = الأذن — تعرف كيف تسمع وتفهم الصوت
    recognizer = sr.Recognizer()

    # sr.Microphone() = يفتح المايك
    # with = يضمن يغلق المايك تلقائياً بعد الانتهاء
    with sr.Microphone() as source:
        print("🎤 Listening...")

        # تستمع للغرفة ثانية وحدة قبل ما تسجل
        # ليش؟ علشان تتعلم شنو هو الصوت الخلفي (مكيف، شارع...)
        # وتتجاهله لما تسمع كلامك
        recognizer.adjust_for_ambient_noise(source, duration=1)

        recognizer.pause_threshold = 2.0
        recognizer.energy_threshold = 300

        # تسجل صوتك وتوقف لما تسكت
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)

    try:
        # ترسل التسجيل لـ Google وترجعه نص — مجاني بدون API key
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text

    except sr.UnknownValueError:
        # ما فهمت شي — صوت غير واضح
        print("Didn't catch that, try again!")
        return None

    except sr.RequestError:
        # مشكلة بالإنترنت — Google مو متاح
        print("Network error, check your connection!")
        return None