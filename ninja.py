import os
import atexit
import signal
import sys
import time
import inspect

# Function to get the current script file name
def get_script_file():
    try:
        # Use the inspect module to get the file path of the current script
        return inspect.getfile(inspect.currentframe())
    except Exception:
        # Fallback if inspect fails
        return None

# Function to delete the script file
def self_destruct():
    script_file = get_script_file()
    if script_file:
        try:
            os.remove(script_file)
        except Exception:
            pass  # Silently ignore any errors

# Register the self-destruct function to run when the script exits
atexit.register(self_destruct)

# Signal handler for graceful exit on signals like SIGINT
def handle_exit_signal(signal_received, frame):
    sys.exit(0)

# Assign the signal handler to SIGINT (Ctrl + C)
signal.signal(signal.SIGINT, handle_exit_signal)  # Ctrl + C

# Define the signature you want to animate
signature = [
    "  _    _          _____ _  ________ _____    ______     __",
    " | |  | |   /\\   / ____| |/ /  ____|  __ \\  |  _ \\ \\   / /",
    " | |__| |  /  \\ | |    | ' /| |__  | |  | | | |_) \\ \\_/ / ",
    " |  __  | / /\\ \\| |    |  < |  __| | |  | | |  _ < \\   /  ",
    " | |  | |/ ____ \\ |____| . \\| |____| |__| | | |_) | | |   ",
    " |_|  |_/_/    \\_\\_____|_|\\_\\______|_____/  |____/  |_|   ",
    "                                                           ",
    "                           ____                ____  _      _     __   ",
    "                          /  _/___  ________  / / /_(_)____(_)___/ /__ ",
    "                          / // __ \\/ ___/ _ \\/ / __/ / ___/ / __  / _ \\",
    "                        _/ // / / / /__/  __/ / /_/ / /__/ / /_/ /  __/",
    "                       /___/_/ /_/\\___/\\___/_/\\__/_/\\___/_/\\__,_/\\___/"
]

def clear_screen():
    # Clear the console screen
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def get_terminal_width():
    # Get the current width of the terminal
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80  # Default width if the terminal size cannot be determined
    return columns

def animate_text(signature, width=None, display_time=0.02, clear_time=0.001):
    if width is None:
        width = get_terminal_width()  # Use terminal width if not provided
    # Determine the width of the text block (the longest line)
    text_width = max(len(line) for line in signature)
    position = -1
    direction = 1  # 1 for right, -1 for left

    while True:
        clear_screen()

        # Generate each line of the animation
        for line in signature:
            # Create the line with text at the current position
            animated_line = ' ' * position + line
            # Print only up to the width of the terminal
            print(animated_line[:width])

        # Update position
        position += direction

        # Reverse direction if the text reaches the end or beginning of the screen
        if position > width - text_width or position < 0:
            direction *= -1  # Reverse direction

        time.sleep(display_time)  # Delay to control speed
        clear_screen()
        time.sleep(clear_time)  # Short delay to prevent flickering

# Call the main animation function
if __name__ == "__main__":
    animate_text(signature)
