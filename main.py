import datetime
import webbrowser
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"CORTEX: {text}")
    engine.say(text)
    engine.runAndWait()

def greet():
    speak("Hello Hibban. I am ready. How can I assist you?")

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def process_command(command):
    if command == "hello":
        speak("Hello! What can I do for you?")

    elif command == "time":
        get_time()

    elif command == "open google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif command == "open youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif command == "open sfsu":
        speak("Opening S F S U website")
        webbrowser.open("https://www.sfsu.edu")

    elif command == "bye":
        speak("Shutting down. Goodbye!")
        return False

    else:
        speak("Sorry, I don't understand that command.")

    return True

def run_assistant():
    greet()

    running = True
    while running:
        command = input("You: ").strip().lower()
        running = process_command(command)

if __name__ == "__main__":
    run_assistant()