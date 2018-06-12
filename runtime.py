import downloader_class as dc
import screen_setup as ss
import time
from threading import Thread
import curses
import os
import sys
import random
import distro_obj as dis
##
# Runtime.py Script is designed to simulate a hot dog downloader race
##

url_array, url_array_os = dis.choose_racers()

# Setting Up colors and Terminal Res Tracker.
screen, red, yellow_background, blue, default, yellow_text, cyan_dots = ss.curses_setup()
window_height, window_width = ss.window_res(screen)

def func():

    # Firt try except is used to display the countdown screen before race
    try:
        for x in range(3, 0, -1):
            count = 0
            while(count != 1000):
                middle_height, middle_width = ss.window_res(screen)
                screen.clear()
                screen.border()
                screen.addstr(middle_height - 2, middle_width - 22 ,
                    '(>0.0)>   -_-_COUNTDOWN HYPE_-_-   <(0.0<)', curses.color_pair(yellow_background))
                screen.addch(middle_height, middle_width - 1, str(x) , curses.color_pair(yellow_background))
                screen.refresh()
                count += 1

        count1 = 0
        while(count1 != 1000):
            middle_height, middle_width = ss.window_res(screen)
            screen.clear()
            screen.border()
            screen.addstr(middle_height - 2, middle_width - 22 ,
                '(>0.0)>   -_-_COUNTDOWN HYPE_-_-   <(0.0<)', curses.color_pair(yellow_background))
            screen.addstr(middle_height, middle_width - 2, 'GO!', curses.color_pair(yellow_background))
            screen.refresh()
            count1 += 1

        screen.clear()

    # For user wanting to ctr ^C in countdown window
    except KeyboardInterrupt:
        curses.endwin()
        sys.exit("Keyboard Interrupt, Quitting...")

    # Declaring an array of players and instantiating those players and setting url total length
    players = []
    for i in range(0, 5, 1):
        players.append(dc.Downloader())

    # Declaring an array of threads
    threads = []
    index = 0
    for p in players:
        threads.append(Thread(target=p.download, args=(url_array[index], url_array_os, index)))
        index += 1

    # Starting the array of threads
    for thread in threads:
        thread.start()

    # Setting color for the race window
    screen.bkgd(curses.color_pair(default))

    try:
        max_download_speed = 0
        split_timer = time.time()
        start_time = time.time()

        while(True):
            # Setting middle_width and height
            middle_height, middle_width = ss.window_res(screen)

            # Getting window size
            window_height, window_width = screen.getmaxyx()

            # Clearing each for each new frame of print
            screen.clear()

            # Displaying border
            screen.border()

            percent_print = []
            for p in players:
                percent_print.append(int((window_width - 23) * p.data_length/p.total_length))

            # Determing peak_download and highest overall peak_download
            for p in players:
                p.peak_download = (p.chunk_rate/1024/1024)
                if p.peak_download > max_download_speed:
                    max_download_speed = p.peak_download

            # Displaying overall peak download to screen
            screen.addstr(36, 2, "Overall Peak Download Rate Recorded: ", curses.color_pair(blue))
            screen.addstr(36, 39, "%.3f Mbs" % (max_download_speed), curses.color_pair(yellow_text))

            # Title for the race window
            screen.addstr(2, middle_width - 10, "Hot Dog Downloader", curses.color_pair(blue))
            screen.addstr(3, middle_width - 14, '--------------------------', curses.color_pair(blue))

            # Y componet offset for players X ussed in percent_print array
            y_offset    = 6
            x           = 0

            for p in players:

                # Displaying the player, rate, percent downloaded and start/finish animation
                screen.addstr(y_offset, 2,  "Player"+str(x+1)+" ::", curses.color_pair(cyan_dots))
                screen.addstr(y_offset, 13, "| Rate: %.3f MBs" %
                    (round(p.chunk_rate/1024/1024, 3)))
                screen.addstr(y_offset, 31, "| Percent Downloaded: %s%%" % (p.get_percent_done()))
                screen.addstr(y_offset+2, 2, "start |%s:]%s| finish!" %
                    ('-' * percent_print[x], ' ' *(window_width - 23 - percent_print[x])),
                    curses.color_pair(yellow_text))

                # Displaying the peak download
                if(p.chunk_rate > p.peak_download_high):
                    p.peak_download_high = p.chunk_rate
                screen.addstr(y_offset+4, 2, "Peak Download Rate Recorded:", curses.color_pair(blue))
                screen.addstr(y_offset+4, 34, "%.3f Mbs" % (p.peak_download_high/1024/1024), curses.color_pair(yellow_text))

                # If done hen print static image for load animation but can still be resized
                if(p.get_percent_done() == 100):
                    screen.addstr(y_offset, 21, "0.000", curses.color_pair(red))
                    screen.addstr(y_offset+2, 2, "start |%s:]%s| finish!" %
                        ('-' * percent_print[x], ' ' *(window_width - 22 - percent_print[x])),
                        curses.color_pair(yellow_text))
                    p.done_flag = True

                # Display overall average download when done
                if(p.done_flag == True and p.get_percent_done() == 100):
                    if(p.stop_avg_flag == False):
                        p.time_end = time.time()
                        p.stop_avg_flag = True
                    p.overall_average_download = round(((p.total_length /(p.time_end - start_time)) /1024/1024), 3)
                    screen.addstr(y_offset+4, 46, "Overall Average Download Speed:", curses.color_pair(blue))
                    screen.addstr(y_offset+4, 81, "%.3f MBs" % (p.overall_average_download), curses.color_pair(yellow_text))
                else:
                    pass

                # Offesting the next racer in y-direction and updating x for player percent_print array
                y_offset    += 6
                x           += 1
            screen.refresh()
            time.sleep(.1)

    # If User Ctr ^C, threads will get celaned up and exit
    except KeyboardInterrupt:
        for p in players:
            p.run_thread = False
        curses.endwin()
        sys.exit("Keyboard Interrupt, Quitting...")

func()
