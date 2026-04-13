import datetime

def greet():
    print("CORTEX: Hello Hibban. I am ready. How can I assist you?")

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"CORTEX: The current time is {current_time}")

def process_command(command):
    if command == "hello":
        print("CORTEX: Hello! What can I do for you?")
    
    elif command == "time":
        get_time()
    
    elif command == "bye":
        print("CORTEX: Shutting down. Goodbye!")
        return False
    
    else:
        print("CORTEX: Sorry, I don't understand that command.")
    
    return True

def run_assistant():
    greet()
    
    running = True
    while running:
        command = input("You: ").lower()
        running = process_command(command)

if __name__ == "__main__":
    run_assistant()