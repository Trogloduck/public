import curses
from curses import wrapper

#stfscrn : standard screen

def main(stdscr):
    stdscr.clear() #clear the screen
    

wrapper(main)