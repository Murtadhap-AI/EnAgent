
import pyttsx3

engine = pyttsx3.init()  # ← مرة وحدة بأعلى الملف

for voice in engine.getProperty('voices'):
    if "english" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break
engine.setProperty('rate', 150)

def speak(text: str) -> None:
    engine.say(text)
    engine.runAndWait()