import speech_recognition as sr
from assistant.speech import speak

def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("CORTEX: Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("I did not hear anything.")
            return ""

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:
        speak("Speech service is not available right now.")
        return ""