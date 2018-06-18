import curses

##
# Screen_Setup purpose is to setup the screen for runtime.py
##

def curses_setup():

    # Instantiating screen object
    screen = curses.initscr()

    # Cursor visibility = false
    curses.curs_set(0)

    # Starting and declaring colors for the program
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)

    red                 = 1 # Red text with black background
    yellow_background   = 2 # Yellow background hurts eyes
    blue                = 3 # Blue text black background
    default             = 4 # Green text with black background
    yellow_text         = 5 # Yellow text with black bacground
    cyan_dots           = 6 # Blue dots when race is done

    # Setting bacground color for first window launch
    screen.bkgd(curses.color_pair(yellow_background))
    return screen, red, yellow_background, blue, default, yellow_text, cyan_dots


# Window_res determines middle_height, middle_width, pos_start x
def window_res(screen):

    window_height, window_width = screen.getmaxyx()
    middle_height = (round(window_height/2 - 1))
    middle_width = (round(window_width/2 -1))
    pos_start_x = (window_width -1)

    return middle_height, middle_width
