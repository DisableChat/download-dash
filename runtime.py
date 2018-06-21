import downloader_class as dc
import screen_setup as ss
import distro_obj as dis
from downloader_class import Downloader
import hotdog as hd
import time
from threading import Thread
import curses
import os
import sys
import random
import subprocess
from subprocess import DEVNULL, STDOUT, run, Popen
##
# Runtime.py Script is designed to simulate a hot dog downloader race
##

url_array, url_array_os = dis.choose_racers()

# Setting Up colors and Terminal Res Tracker.
screen, red, yellow_background, blue, default, yellow_text, cyan_dots = ss.curses_setup()
window_height, window_width = ss.window_res(screen)

def player_setup():
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
        return players, threads

def func():

    players, threads = player_setup()
    dis.players_array = players

    # Print to screen pre intro 
    hd.print_pre_intro()

    # Odds screen display to terminal
    hd.odds_screen()

    #initial screen with countdown
    hd.print_hotdog()

    # Starting the array of threads
    for thread in threads:
        thread.start()

    # Setting color for the race window
    screen.bkgd(curses.color_pair(default))

    try:
        finish_flag         = False
        ranking_x_offset    = 24
        max_download_speed  = 0
        split_timer         = time.time()
        start_time          = time.time()

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
            screen.addstr(46, 13, "| Overall Peak Download Rate Recorded: ", curses.color_pair(blue))
            screen.addstr(46, 52, "%.3f MBs" % (max_download_speed), curses.color_pair(yellow_text))

            # Title for the race window
            screen.addstr(1, middle_width - 13, '========================', curses.color_pair(yellow_text))
            screen.addstr(2, middle_width - 14, '(-- Hot Dog Downloader --)', curses.color_pair(red))
            screen.addstr(3, middle_width - 13, '========================', curses.color_pair(yellow_text))

            screen.addstr(1, middle_width + 23, '======================', curses.color_pair(yellow_text))
            screen.addstr(2, middle_width + 22, '(- LIVE RANKINGS BOII -)', curses.color_pair(red))
            screen.addstr(3, middle_width + 23, '======================', curses.color_pair(yellow_text))
            screen.addstr(3, middle_width + 48, 'MIN|SEC|MS', curses.A_UNDERLINE)
            screen.addstr(4, middle_width + ranking_x_offset, '1st Place ::', curses.A_BOLD)
            screen.addstr(5, middle_width + ranking_x_offset, '2nd Place ::', curses.A_BOLD)
            screen.addstr(6, middle_width + ranking_x_offset, '3rd Place ::', curses.A_BOLD)
            screen.addstr(7, middle_width + ranking_x_offset, 'Hard Rip  ::', curses.A_BOLD)
            screen.addstr(8, middle_width + ranking_x_offset, 'Mega Rip  ::', curses.A_BOLD)

            # Y componet offset for players X ussed in percent_print array
            y_offset    = 11
            j           = 4
            x           = 0

            for p in players:

                # Displaying the OS being downloaded for player
                screen.addstr(y_offset+4, 13, "| OS: ", curses.COLOR_WHITE)
                screen.addstr(y_offset+4, 20, str(dis.url_array_random_os[x]), curses.A_BOLD)

                # Displaying File Name
                screen.addstr(y_offset+4, 33, "| File: ", curses.COLOR_WHITE)
                screen.addstr(y_offset+4, 41, str(dis.five_files[x]),curses.A_BOLD)

                # Displaying size of file being downloaded
                screen.addstr(y_offset+4, 89, "| Size: ", curses.color_pair(red))
                screen.addstr(y_offset+4, 98, str(round(p.total_length/1024/1024,2)) + ' MB', curses.color_pair(blue))

                # Displaying the player, rate, percent downloaded and start/finish animation
                screen.addstr(y_offset, 2,  "Player"+str(x+1)+" ::", curses.color_pair(cyan_dots))
                screen.addstr(y_offset, 13, "| Rate: %.3f MBs" %
                    (round(p.chunk_rate/1024/1024, 3)))
                screen.addstr(y_offset, 33, "| Percent Downloaded: %s%%" % (p.get_percent_done()))
                screen.addstr(y_offset+5, 2, "start |%s:]%s| finish!" %
                    ('-' * percent_print[x], ' ' *(window_width - 23 - percent_print[x])),
                    curses.color_pair(yellow_text))

                # Displaying the peak download
                if(p.chunk_rate > p.peak_download_high):
                    p.peak_download_high = p.chunk_rate
                screen.addstr(y_offset+2, 13, "| Peak Download Rate Recorded:", curses.color_pair(blue))
                screen.addstr(y_offset+2, 43, " %.3f MBs" % (p.peak_download_high/1024/1024), curses.color_pair(yellow_text))

                # If done hen print static image for load animation but can still be resized
                if(p.get_percent_done() == 100):
                    screen.addstr(y_offset, 20, " 0.000", curses.color_pair(red))
                    screen.addstr(y_offset+5, 2, "start |%s:]%s| finish!" %
                        ('-' * percent_print[x], ' ' *(window_width - 22 - percent_print[x])),
                        curses.color_pair(yellow_text))
                    j += 1
                    p.done_flag = True

                # Display overall average download when done
                if(p.done_flag == True and p.get_percent_done() == 100):

                    if(finish_flag == False):
                        # playing airhorn
                        with open(os.devnull, 'wb') as devnull:
                            subprocess.Popen(['aplay', dis.file_directory + 'horn.wav'], stdout=devnull, stderr=subprocess.STDOUT)
                            finish_flag = True

                    if(p.stop_avg_flag == False):
                        p.time_end = time.time()
                        p.stop_avg_flag = True
                        p.ranking_array.append(str(x+1))

                        # Displaying the finish times for the racers
                        ms_first = round((p.time_end -start_time)*1000, 0)
                        dc.timing_array.append(dc.get_time(ms_first))

                    p.overall_average_download = round(((p.total_length /(p.time_end - start_time)) /1024/1024), 3)
                    screen.addstr(y_offset+2, 56, "| Overall Average Download Speed:", curses.color_pair(blue))
                    screen.addstr(y_offset+2, 89, " %.3f MBs" % (p.overall_average_download), curses.color_pair(yellow_text))

                    screen.addstr(j-1, middle_width + ranking_x_offset + 13, 'Player ', curses.color_pair(red))
                    screen.addstr(j-1, middle_width + ranking_x_offset + 20, str(p.ranking_array[j-5]), curses.color_pair(yellow_text))
                    screen.addstr(j-1, middle_width + ranking_x_offset + 25, str(dc.timing_array[j-5]), curses.A_BOLD)

                else:
                    pass

                # Offesting the next racer in y-direction and updating x for player percent_print array
                y_offset    += 7
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
