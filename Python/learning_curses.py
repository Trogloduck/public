import curses
from curses import wrapper
import time

def main(stdscr):
    """
    1st create color pairs (background, then color of letters)
    """
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # define a color pair
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # define a color pair
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK) # define a color pairpair
    """
    Creating variables to call each color pattern quicker
    """
    GREEN_AND_BLACK = curses.color_pair(1)
    RED_AND_BLACK = curses.color_pair(2)
    BLUE_AND_BLACK = curses.color_pair(3)

    """
    Function will display numbers in different colors
    depending if they are even or odd
    """
    height = curses.LINES()
    width = curses.COLS()

    for i in range(100):
        stdscr.clear() # clears the screen
        color = GREEN_AND_BLACK
        if i%2 == 0:
            color = RED_AND_BLACK
        stdscr.addstr(, width//2, f"Count: {i}", color)
        stdscr.refresh() # refreshes the screen (displays next)
        time.sleep(0.1)

    stdscr.getch() # get a character from the user to exit the program

wrapper(main)