import pyttsx3

def speak(text):
    print(f"CORTEX: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()