# implementation
import downloader_class as dc
import time
from threading import Thread
import curses
import os

##
# Determining file size before download and also downloading file from url
# While also displaying the horse running(downloading

url1 = 'http://ipv4.download.thinkbroadband.com/5MB.zip'
url2 = 'http://ipv4.download.thinkbroadband.com/10MB.zip'
url3 = 'http://ipv4.download.thinkbroadband.com/20MB.zip'
url4 = 'http://ipv4.download.thinkbroadband.com/50MB.zip'
url5 = 'http://ipv4.download.thinkbroadband.com/100MB.zip'
#url = 'https://www.sample-videos.com/img/Sample-jpg-image-1mb.jpg'
#url2 = 'https://www.sample-videos.com/img/Sample-jpg-image-5mb.jpg' # hard coding url from now
#url3 = 'https://www.sample-videos.com/img/Sample-jpg-image-30mb.jpg'
#url4 = 'https://www.sample-videos.com/img/Sample-jpg-image-1mb.jpg'

##
# Setting Up colors and Terminal Res Tracker.
##--------------------------------------------------------------------------------------------------------#

screen = curses.initscr() # instantiating screen object
curses.curs_set(0) # Cursor visibility = false

# starting and declaring colors for the program
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

# Window_res determines middle_height, middle_width, pos_start x
def window_res(screen):
    window_height, window_width = screen.getmaxyx() # getting window size
    middle_height = (round(window_height/2 - 1)) # middle window height
    middle_width = (round(window_width/2 -1)) # middle window width
    pos_start_x = (window_width -1)
    return middle_height, middle_width

window_height, window_width = window_res(screen)

screen.bkgd(curses.color_pair(yellow_background)) # setting bacground color for first window launch

#----------------------------------------------------------------------------------------------------------#

def func():

    # firt try is used to display the countdown screen before race
    try:
        for x in range(3, 0, -1):
            count = 0
            while(count != 1000):
                middle_height, middle_width = window_res(screen)
                screen.clear()
                screen.border()
                screen.addstr(middle_height - 2, middle_width - 22 ,
                    '(>0.0)>   -_-_COUNTDOWN HYPE_-_-   <(0.0<)', curses.color_pair(yellow_background))
                screen.addch(middle_height, middle_width - 1, str(x) , curses.color_pair(yellow_background))
                screen.refresh()
                count += 1

        count1 = 0
        while(count1 != 1000):
            middle_height, middle_width = window_res(screen)
            screen.clear()
            screen.border()
            screen.addstr(middle_height - 2, middle_width - 22 ,
                '(>0.0)>   -_-_COUNTDOWN HYPE_-_-   <(0.0<)', curses.color_pair(yellow_background))
            screen.addstr(middle_height, middle_width - 2, 'GO!', curses.color_pair(yellow_background))
            screen.refresh()
            count1 += 1

        screen.clear()
    except KeyboardInterrupt: # for user wanting to ctr ^C
        curses.endwin()
        sys.exit()

    # Declaring an array of players and instantiating those players and setting url total length
    players = []
    for i in range(0, 5, 1):
        players.append(dc.Downloader())

    # declaring an array of threads
    threads = []
    for p in players:
        threads.append(Thread(target=p.download, args=(url4,)))


    # starting the array of threads
    for thread in threads:
        thread.start()

    screen.bkgd(curses.color_pair(default)) # setting color for the race window

    try:
        max_download_speed = 0
        start_time = time.time()

        while(True):

            middle_height, middle_width = window_res(screen)
            window_height, window_width = screen.getmaxyx() # getting window size

            screen.clear() # clearing each for each new frame of print
            screen.border() # displaying border

            percent_print = []
            for p in players:
                percent_print.append(int((window_width - 23) * p.data_length/p.total_length))

            # determing peek_download and highest overall peek_download
            for p in players:
                p.peek_download = (round(p.get_data_length()/(time.time()+1 -start_time)/1024/1024, 3))
                if p.peek_download > max_download_speed:
                    max_download_speed = p.peek_download

            # Displaying overall peek download to screen
            screen.addstr(36, 2, "Overall Peek Download Rate Recorded: ", curses.color_pair(blue))
            screen.addstr(36, 39, "%.3f Mbs" % (max_download_speed), curses.color_pair(yellow_text))

            # Title for the race window
            screen.addstr(2, middle_width - 7, "Hot Dog Racer", curses.color_pair(blue))
            screen.addstr(3, middle_width - 14, '--------------------------', curses.color_pair(blue))
            screen.addstr(3, middle_width, (str(players[0].total_length)))
            screen.addstr(3, middle_width - 10, (str(players[0].data_length)))
            y_offset = 6
            x = 0
            for p in players:

                screen.addstr(y_offset, 2,  "Player1 ::", curses.color_pair(cyan_dots))
                screen.addstr(y_offset, 13, "| Rate: %.3f MBs" %
                    (round(p.get_data_length()/(time.time()+1 -start_time)/1024/1024, 3)))
                screen.addstr(y_offset, 31, "| Percent Downloaded: %s%%" % (p.get_percent_done()))
                screen.addstr(y_offset+2, 2, "start |%s:]%s| finish!" %
                    ('-' * percent_print[x], ' ' *(window_width - 23 - percent_print[x])),
                    curses.color_pair(yellow_text))

                if(p.peek_download > p.peek_download_high):
                    p.peek_download_high = p.peek_download
                screen.addstr(y_offset+4, 2, "Peek Download Rate Recorded:", curses.color_pair(blue))
                screen.addstr(y_offset+4, 34, "%.3f Mbs" % (p.peek_download_high), curses.color_pair(yellow_text))

                if(p.get_percent_done() == 100):
                    screen.addstr(y_offset, 21, "0.000", curses.color_pair(red))
                    screen.addstr(y_offset+2, 2, "start |%s:]%s| finish!" %
                        ('-' * percent_print[x], ' ' *(window_width - 22 - percent_print[x])),
                        curses.color_pair(yellow_text))

                    if(p.overall_average_download == 0):
                        p.overall_average_download = round(p.total_length /(time.time() + 1  - start_time) /1024/1024, 3)
                    screen.addstr(y_offset+4, 46, "Overall Average Download Speed:", curses.color_pair(blue))
                    screen.addstr(y_offset+4, 81, "%.3f MBs" % (p.overall_average_download), curses.color_pair(yellow_text))

                y_offset += 6 # offesting the next racer in y-direction
                x += 1
            screen.refresh()
            time.sleep(.1)

    except KeyboardInterrupt:
        curses.endwin()
        sys.exit()

func()
