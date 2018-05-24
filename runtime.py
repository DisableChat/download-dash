# implementation
import downloader_class as dc
import sys
import time
from threading import Thread
import curses
import os

##
# Determining file size before download and also downloading file from url
# While also displaying the horse running(downloading animation)
##

url = 'https://www.sample-videos.com/img/Sample-jpg-image-1mb.jpg'
url2 = 'https://www.sample-videos.com/img/Sample-jpg-image-5mb.jpg' # hard coding url from now
url3= 'https://www.sample-videos.com/img/Sample-jpg-image-30mb.jpg'

#attempting to create thread so we can print the player1 downalad
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_YELLOW)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)

red = 1 # red text with black background
yellow_background = 2 # yellow background hurts eyes
blue = 3 # blue text black background
default = 4 # green text with black background
yellow_text = 5 # yellow text with black bacground
cyan_dots = 6 # blue dots when race is done

screen.bkgd(curses.color_pair(yellow_background)) # setting bacground color for first window launch

# curses early stages/messing around
def func():

    #  the first try/except is printing the countdown window when you first launch
    try:
        screen.border()
        countdown = True
        while(countdown == True):
            screen.addstr(8, 52, '(>0.0)>   -_-_COUNTDOWN HYPE_-_-   <(0.0<)', curses.color_pair(yellow_background))
            screen.addch(12, 73, '3', curses.color_pair(yellow_background))
            screen.refresh()
            time.sleep(1)
            screen.addch(12, 73, '2', curses.color_pair(yellow_background))
            screen.refresh()
            time.sleep(1)
            screen.addch(12, 73, '1', curses.color_pair(yellow_background))
            screen.refresh()
            time.sleep(1)
            screen.addstr(12, 73, 'GO!', curses.color_pair(yellow_background))
            screen.refresh()
            screen.addstr(12, 73, '   ')
            screen.addstr(8, 52, '                                           ')
            countdown = False
    except KeyboardInterrupt: # for user wanting to ctr ^C
        curses.endwin()
        sys.exit()

    # instations of the donwnloader class and starting threads for the objects
    player1 = dc.Downloader()
    player2 = dc.Downloader()
    player1.set_total_length(url)
    player2.set_total_length(url2)
    thread1 = Thread(target=player1.set_data_length, args=(url,))
    thread2 = Thread(target=player2.set_data_length, args=(url2,))
    thread1.start()
    thread2.start()

    screen.bkgd(curses.color_pair(default)) # setting color for the race window

    try:
        loading = '.'
        bool = True
        start_time1 = time.time()
        while(bool == True):
            screen.border()

            # player 1 and player 2 percent for printing
            player1_percent_done = int(50 * player1.data_length/player1.total_length)
            player2_percent_done = int(50 * player2.data_length/player2.total_length)

            # Title for the race window
            screen.addstr(2,45,                     "WE GONA RACE TODAY COACH", curses.color_pair(blue))
            screen.addstr(3,20, '-------------------------------------------------------------------------', curses.color_pair(blue))

            #player 1
            screen.addstr(6, 2, "Player1 ::", curses.color_pair(cyan_dots))
            screen.addstr(6, 13, "| Rate: %.3f MBs" % (round(player1.get_data_length()/(time.time()+1 -start_time1)/1024/1024, 3)))
            screen.addstr(6, 31, "| Percent Downloaded: %s%%" % (2*player1_percent_done))
            screen.addstr(6, 53, "start |%s:]%s| finish!" % ('-' * player1_percent_done, ' ' *(50-player1_percent_done)), curses.color_pair(yellow_text))
            if(player1.data_length == player1.total_length):
                screen.addstr(6, 21, "0.000", curses.color_pair(red))
                winner = player1

            # player 2
            screen.addstr(8, 2, "Player2 ::" , curses.color_pair(cyan_dots))
            screen.addstr(8, 13, "| Rate: %.3f MBs" % (round(player2.get_data_length()/(time.time()+1 - start_time1)/1024/1024, 3)))
            screen.addstr(8, 31, "| Percent Downloaded: %s%%" % (2*player2_percent_done))
            screen.addstr(8, 53, "start |%s:]%s| finish!" % ('-' * player2_percent_done, ' ' *(50-player2_percent_done)), curses.color_pair(yellow_text))
            if(player2.data_length == player2.total_length):
                screen.addstr(8, 21, "0.000", curses.color_pair(red))
                winner = player2

            # If both players finish print loading animation infinitly
            if(player1.data_length == player1.total_length and player2.data_length == player2.total_length ):
                while(True):
                    screen.addstr(20, 50, loading)
                    loading += '  .'
                    screen.refresh()
                    time.sleep(.25)
                    if(loading == '.  .  .  .  .  .  .'):
                        screen.addstr(20, 50, '                   ')
                        screen.refresh()
                        loading = '.'
                    screen.refresh()
                    time.sleep(.25)

            screen.refresh()
            time.sleep(.1)
    except KeyboardInterrupt:
        curses.endwin()
        sys.exit()

func()
