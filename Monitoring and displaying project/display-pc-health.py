import curses
from curses import wrapper
import time
import psutil


def cpu_ram_disk(stdscr, max_width, BLUE_AND_BLACK):
    """
    Display CPU, RAM usage and disk usage
    """
    while True:
        # gather data
        cpu_percent = psutil.cpu_percent(interval=1)
        ram_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent

        # calculate bar width
        cpu_bar_width = int((cpu_percent / 100) * max_width)
        ram_bar_width = int((ram_percent / 100) * max_width)
        disk_bar_width = int((disk_percent / 100) * max_width)

        # create windows
        cpu_window = curses.newwin(3, max_width, 0, 0)
        cpu_border = cpu_window.border()

        ram_window = curses.newwin(3, max_width, 5, 0)
        ram_border = ram_window.border()

        disk_window = curses.newwin(3, max_width, 10, 0)
        disk_border = disk_window.border()

        # display title and bars
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


def top_processes(stdscr):
    """
    Display top 5 processes
    """
    while True:

        # gather data
        processes = {p.pid: p.info for p in psutil.process_iter(['name', 'username'])}
        processes = sorted(processes.items(), key=lambda x: x[1]['memory_percent'], reverse=True)

        # create windows
        top_processes_window = curses.newwin(5, curses.COLS, 16, 0)
        top_processes_window.border()
        top_processes_window.addstr(0, 0, "Top 5 Processes", curses.A_BOLD)
        top_processes_window.refresh()

        # display top 5 processes
        for i, (pid, process) in enumerate(processes[:5]):
            stdscr.addstr(16 + i, 0, f"{i + 1}. {process['name']}, {process['username']}", curses.A_BOLD)
            stdscr.refresh()

        time.sleep(1)
        stdscr.clear()
        stdscr.refresh()


def Main(stdscr):

    max_width = (curses.COLS) - 1
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLUE)
    BLUE_AND_BLACK = curses.color_pair(3)

    cpu_ram_disk(stdscr, max_width, BLUE_AND_BLACK)
    top_processes(stdscr)


wrapper(Main)