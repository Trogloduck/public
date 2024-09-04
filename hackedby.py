import time
import sys
import os
import signal

signature = [
    "  _    _          _____ _  ________ _____    ______     __",
    " | |  | |   /\   / ____| |/ /  ____|  __ \\  |  _ \\ \\   / /",
    " | |__| |  /  \\ | |    | ' /| |__  | |  | | | |_) \\ \\_/ / ",
    " |  __  | / /\\ \\| |    |  < |  __| | |  | | |  _ < \\   /  ",
    " | |  | |/ ____ \\ |____| . \\| |____| |__| | | |_) | | |   ",
    " |_|  |_/_/    \\_\\_____|_|\_\______|_____/  |____/  |_|   ",
    "                                                           ",
    "                           ____                ____  _      _     __   ",
    "                          /  _/___  ________  / / /_(_)____(_)___/ /__ ",
    "                          / // __ \\/ ___/ _ \\/ / __/ / ___/ / __  / _ \\",
    "                        _/ // / / / /__/  __/ / /_/ / /__/ / /_/ /  __/",
    "                       /___/_/ /_/\\___/\\___/_/\\__/_/\\___/_/\\__,_/\\___/"
]


# Define a signal handler that ignores SIGINT (Ctrl + C)
def ignore_interrupt(signal_received, frame):
    print("Nice try ;)")

# Override the default SIGINT handler
signal.signal(signal.SIGINT, ignore_interrupt)


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

def animate_text(signature,  width = get_terminal_width(), display_time=0.02, clear_time=0.001):
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

while True:
    animate_text(signature)

# to get the file from github through powershell execute the following line:
# curl -o "name I want to give to the file" "https://raw.githubusercontent.com/Trogloduck/public_repo/main/hackedby.py"