import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr

def speak(text):
    print(f"CORTEX: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

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

def greet():
    speak("Hello Hibban. I am ready. How can I assist you?")

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def clean_command(command):
    command = command.strip().lower()

    if command.startswith("cortex "):
        command = command.replace("cortex ", "", 1)
    elif command == "cortex":
        command = ""

    return command

def process_command(command):
    if not command:
        return True

    if "hello" in command or "hi" in command or "hey" in command:
        speak("Hello! What can I do for you?")

    elif "time" in command:
        get_time()

    elif "open google" in command or ("google" in command and "open" in command):
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command or ("youtube" in command and "open" in command):
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open sfsu" in command or ("sfsu" in command and "open" in command):
        speak("Opening S F S U website")
        webbrowser.open("https://www.sfsu.edu")

    elif "bye" in command or "exit" in command or "quit" in command:
        speak("Shutting down. Goodbye!")
        return False

    else:
        speak("Sorry, I don't understand that command.")

    return True

def run_assistant():
    greet()

    running = True

    while running:
        mode = input("Type 'text' to type or 'voice' to speak: ").strip().lower()

        if mode == "text":
            command = input("You: ").strip().lower()

        elif mode == "voice":
            command = listen_command()

        else:
            speak("Please choose text or voice.")
            continue

        command = clean_command(command)
        running = process_command(command)

if __name__ == "__main__":
    run_assistant()