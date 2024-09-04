import time
import sys
import os


prompt = "Please enter a number for the countdown:"

# Print prompt one character at a time
for char in prompt:
    print(char, end='', flush=True)
    time.sleep(0.035)  # Adjust delay between characters


user_input = input()  # Cursor will be on same line

feedback = f"\nYou entered: {user_input}\n"

for char in feedback:
    print(char, end='', flush=True)
    time.sleep(0.035)  # Delay 

time.sleep(1)

number = int(user_input) # Convert string to integer

warning = "\nBy entering this number you have activated the countdown\nfor self-destruction of the device on which\nyou are executing this program, take cover.\n\n"
for char in warning:
    print(char, end='', flush=True)
    time.sleep(0.035)  # Delay

time.sleep(1)

for i in range (number, -1, -1):
    print(i)
    time.sleep(0.5) # Delay

print("\n")

final_message = "Explosion of the device imminent, take cover!"


blinks = 5

for _ in range(blinks):
    # Print message and flush output
    print(final_message, end='\r', flush=True)
    time.sleep(0.3)  # Message visible for 0.3 seconds

    # Clear line by overwriting with spaces and flush output
    print(' ' * len(final_message), end='\r', flush=True)
    time.sleep(0.3)  # Message hidden for 0.3 seconds

print(final_message, "\n")


ascii_art = [
    "██████   ██████   ██████  ███    ███     ██ ██ ██ ",
    "██   ██ ██    ██ ██    ██ ████  ████     ██ ██ ██ ",
    "██████  ██    ██ ██    ██ ██ ████ ██     ██ ██ ██ ",
    "██   ██ ██    ██ ██    ██ ██  ██  ██              ",
    "██████   ██████   ██████  ██      ██     ██ ██ ██ "
]

def blink_ascii_art(ascii_art, delay=0.1, blinks=10):
    rows = len(ascii_art)
    
    for _ in range(blinks):
        # Print ASCII art
        for line in ascii_art:
            print(line)
        sys.stdout.flush()
        time.sleep(delay)
        
        # Move cursor up and clear lines where ASCII art was printed
        for _ in range(rows):
            sys.stdout.write('\033[F')  # Move cursor up one line
            sys.stdout.write('\033[K')  # Clear line
        sys.stdout.flush()
        time.sleep(delay)

    # Print final ASCII art to leave it on screen
    for line in ascii_art:
        print(line)

# Run blinking animation
blink_ascii_art(ascii_art)


print("\nWhy did you just sit there in front of your screen? Now you dead :'(")

input() # Prevents program shutting down