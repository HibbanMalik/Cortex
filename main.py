from assistant.listener import listen_command
from assistant.commands import greet, clean_command, process_command
from assistant.speech import speak

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