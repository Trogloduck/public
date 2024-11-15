import curses
from curses import wrapper
import time
import psutil
import threading


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
        cpu_window.border()

        ram_window = curses.newwin(3, max_width, 5, 0)
        ram_window.border()

        disk_window = curses.newwin(3, max_width, 10, 0)
        disk_window.border()

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


def top_processes(stdscr, max_width):
    """
    Display top 5 processes
    """
    while True:
        # gather data
        processes = {p.pid: p.info for p in psutil.process_iter(['name', 'username', 'memory_percent', 'memory_info'])}
        processes = sorted(processes.items(), key=lambda x: x[1]['memory_percent'], reverse=True)

        # create windows
        top_processes_window = curses.newwin(8, max_width, 16, 0)
        top_processes_window.border()

        # display title and top 5 processes and their memory usage
        top_processes_window.addstr(0, 0, "Top 5 Processes", curses.A_BOLD)
        top_processes_window.refresh()

        for i, (_, process) in enumerate(processes[:5]):
            mem_usage_mb = process['memory_info'].rss / (1024 * 1024)
            top_processes_window.addstr(1 + i, 1, f"{i + 1}. {process['name']}, {process['username']}, {mem_usage_mb:.2f} MB, {process['memory_percent']:.2f}%", curses.A_BOLD)
            top_processes_window.refresh()

        time.sleep(1)
        top_processes_window.clear()
        top_processes_window.refresh()


def Main(stdscr):

    max_width = (curses.COLS) - 1
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLUE)
    BLUE_AND_BLACK = curses.color_pair(3)
    # Run top_processes in a separate thread
    top_processes_thread = threading.Thread(target=top_processes, args=(stdscr, max_width))
    top_processes_thread.daemon = True
    top_processes_thread.start()

    cpu_ram_disk(stdscr, max_width, BLUE_AND_BLACK)
    top_processes(stdscr, max_width)


wrapper(Main)