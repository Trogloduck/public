import curses
from curses import wrapper
import psutil


def Main(stdscr):

    max_width = (curses.COLS // 2) - 1
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
    BLUE_AND_BLACK = curses.color_pair(1)

    cpu_window = curses.newwin(3, max_width//2, 0, 0)
    cpu_border = 

    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        ram_percent = psutil.virtual_memory().percent

        cpu_bar_width = int((cpu_percent / 100) * max_width)
        ram_bar_width = int((ram_percent / 100) * max_width)
        
        stdscr.addstr(0, 0, f"CPU Usage: {cpu_percent:.2f}%", curses.A_BOLD)
        for i in range(0, max_width):
            if i < cpu_bar_width:
                stdscr.addch(1, i, " ", BLUE_AND_BLACK)
            else:
                stdscr.addch(1, i, " ")

        stdscr.addstr(3, 0, f"RAM Usage: {ram_percent:.2f}%", curses.A_BOLD)
        for i in range(0, max_width):
            if i < ram_bar_width:
                stdscr.addch(4, i, " ", BLUE_AND_BLACK)
            else:
                stdscr.addch(4, i, " ")

        stdscr.refresh()

wrapper(Main)