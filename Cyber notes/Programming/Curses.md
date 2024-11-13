```python
"""
Initialization
"""
import curses
from curses import wrapper
import time

# stfscrn : standard screen

def main(stdscr):
    """
    1st create color pairs (background, then color of letters)
    """
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE) # define a color pair
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE) # define a color pair
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_WHITE) # define a color pair
    """
    Creating variables to call each color pattern quicker
    """
    WHITE_AND_BLUE = curses.color_pair(1)
    RED_AND_WHITE = curses.color_pair(2)
    GREEN_AND_WHITE = curses.color_pair(3)

    """
    Function will display numbers in different colors
    depending if they are even or odd
    """
    for i in range(100):
        stdscr.clear() # clears the screen
        color = WHITE_AND_BLUE
        if i%2 == 0:
            color = RED_AND_WHITE
        stdscr.addstr(f"Count: {i}", color)
        stdscr.refresh() # refreshes the screen (displays next)
        time.sleep(0.1)

    stdscr.getch() # get a character from the user to exit the program

wrapper(main)
```

### Initializing
```python
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle # draw rectangles
import time # add delay
```

Getting the screen dimensions:
`curses.LINES`, `curses.COLS`
--> good to subtract 1 to each to display things within the bounds of the screen
### Creating color patterns
```python
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE) # define a color pair
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE) # define a color pair
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_WHITE) # define a color pair
```

### Creating windows
```python
counter_win = curses.newwin(1, 20, 10, 10)
```
 *creates a new window **1** line high, **20** columns wide, at position **10**, **10***
 
### Combining attributes
Use the pipe "|" to combine attributes

### Clearing and refreshing
Clearing allows to clear the screen/window: `stdscr.clear()` / `new_window.clear()` / ...
Refreshing displays the next frame

### Creating a pad
```python
pad = curses.newpad(100, 100) # create a new pad 100x100
    stdscr.refresh() # refresh the screen
    for i in range(100):
        for j in range(26):
            char = chr(65 + j) # get the character from the ASCII table
            pad.addstr(char, GREEN_AND_WHITE) # add the character to the pad with the color pair
    pad.refresh(0, 0, 5, 5, 25, 75) # refresh the pad, shows the pad from 5, 5 to 25, 75
```
(0, 0) is the start of the pad, (5, 5) marks the start of what we display, (25, 75) marks the end of what we display

The pad and its displayed content can be moved using a for loop for instance:
```python
for i in range(curses.LINES-1):
    pad.refresh(0, 0, 5, 5+i, 25, 30+i)
```
*moves the content of the pad horizontally*

```python
for i range(curses.LINES-1):
    pad.refresh(0, i, 5, 5, 25, 30)
```
*moves content displayed horizontally*

### Other functions
```python
stdscr.getkey() # gets key --> actual character
stfscr.getch() # gets character --> number of the character
stdscr.nodelay(True) # make the screen not wait for user input to do stuff
```

### Textbox
```python
win = curses.newwin(3, 18, 2, 2)
box = Textbox(win) # create text editing area, using emacs keybindings
rectangle(stdscr, 1, 1, 5, 20)
stdscr.refresh()

box.edit() # edit the box
text = box.gather().strip().replace("\n", "") # gather the text from the box

stdscr.addstr(7, 3, text, curses.A_REVERSE) # add the text to the screen
```
N.B: coordinates and dimensions are reversed between windows and textboxes

### Adding an attribute
```python
stdscr.attron(GREEN_AND_BLACK)
rectangle(stdscr, 1, 1, 5, 20)
stdscr.addstr(2, 2, "Hello")
stdscr.attroff(GREEN_AND_BLACK)
```

### Adding a border
```python
stdscr.border()
```

### Changing cursor location
```python
stdscr.move(y, x)
```

### Setting up a key to leave the program
```python
while True:
    key = stdscr.getkey()
    if key == "q":
        break
```
