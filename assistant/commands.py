import datetime
import webbrowser
from assistant.speech import speak

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