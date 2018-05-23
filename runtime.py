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

def main():
    player1 = dc.Downloader()
    player2 = dc.Downloader()
    player1.set_total_length(url)
    player2.set_total_length(url2)
    thread1 = Thread(target=player1.set_data_length, args=(url,))
    thread2 = Thread(target=player2.set_data_length, args=(url2,))
    thread1.start()
    thread2.start()
    start_time = time.time()


##
# Uncomment the print_race for player 1 or 2 and they will print, func(player1) is
# testing the implementation of curses
##
    #print_race(player1)
    #print_race(player2)
    func(player1,player2)

    #sys.exit()

# prints the "racing" animation
def print_race(player):
    start_time = time.time()
    while(True):
        var_data = player.get_data_length()
        var_total_data = player.get_total_length()
        done = int(50 * var_data / var_total_data) # done is 50 * data_length divided by total length
        sys.stdout.write("\rRate:   %.3f mbs Percent Downloaded: %s%%  start |%s|:]%s| finish!" %
            (round((var_data/(time.time()- start_time)) /1024/1024, 3), 2*done, '-' * done, ' ' * (50-done)))
        sys.stdout.flush() #makes the terminal output faster by flushing buffer
        time.sleep(.25)
        if(var_data == var_total_data):
            break

# curses early stages/messing around
def func(player1, player2):
    try:
        bool = True
        string1 = "data_length bytes:"
        while(bool == True):
            screen.border()
            #screen.addch(1, 1, '@')
            #screen.addch(3, 29, '@')
            screen.addstr(2,2, "Download's Amount Downloaded So Far")
            screen.addstr(3,2, string1)
            screen.addstr(4,2, string1)
            screen.addstr(3,21, str(player1.data_length))
            screen.addstr(4,21, str(player2.data_length))
            screen.refresh()
    except KeyboardInterrupt:
        curses.endwin()
        sys.exit()

main()
