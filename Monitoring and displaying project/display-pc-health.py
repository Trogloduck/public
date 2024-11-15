import curses
from curses import wrapper
import psutil


def Main(stdscr):

    max_width = (curses.COLS) - 1
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLUE)
    BLUE_AND_BLACK = curses.color_pair(3)

    """
    Display CPU, RAM usage and disk usage
    """
    while True:
        # gathering data
        cpu_percent = psutil.cpu_percent(interval=1)
        ram_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent
        # size of the bars
        cpu_bar_width = int((cpu_percent / 100) * max_width)
        ram_bar_width = int((ram_percent / 100) * max_width)
        disk_bar_width = int((disk_percent / 100) * max_width)

        # creating windows and borders
        cpu_window = curses.newwin(3, max_width, 0, 0)
        cpu_border = cpu_window.border()

        ram_window = curses.newwin(3, max_width, 5, 0)
        ram_border = ram_window.border()

        disk_window = curses.newwin(3, max_width, 10, 0)
        disk_border = disk_window.border()

        # adding title and bars
        cpu_window.addstr(0, 0, f"CPU Usage: {cpu_percent:.2f}%", curses.A_BOLD)
        cpu_window.refresh()

        for i in range(0, max_width):
            if i < cpu_bar_width:
                stdscr.addch(1, i, " ", BLUE_AND_BLACK)
            else:
                stdscr.addch(1, i, " ")

        ram_window.addstr(0, 0, f"RAM Usage: {ram_percent:.2f}%", curses.A_BOLD)
        ram_window.refresh()

        for i in range(0, max_width):
            if i < ram_bar_width:
                stdscr.addch(6, i, " ", BLUE_AND_BLACK)
            else:
                stdscr.addch(6, i, " ")
        stdscr.refresh()

        disk_window.addstr(0, 0, f"Disk Usage: {disk_percent:.2f}%", curses.A_BOLD)
        disk_window.refresh()

        for i in range(0, max_width):
            if i < disk_bar_width:
                stdscr.addch(11, i, " ", BLUE_AND_BLACK)
            else:
                stdscr.addch(11, i, " ")
        stdscr.refresh()


wrapper(Main)