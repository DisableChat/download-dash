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
url3 = 'https://www.sample-videos.com/img/Sample-jpg-image-30mb.jpg'
url4 = 'https://www.sample-videos.com/img/Sample-jpg-image-1mb.jpg'

##
# Setting Up colors and Terminal Res Tracker.
##--------------------------------------------------------------------------------------------------------#
#attempting to create thread so we can print the player1 downalad
screen = curses.initscr()
curses.curs_set(0)
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

def get_win_one_res(screen):
    window_height, window_width = screen.getmaxyx() # getting window size
    middle_height = (round(window_height/2 - 1)) # middle window height
    middle_width = (round(window_width/2 -1)) # middle window width
    return middle_height, middle_width

def get_win_two_res(screen):
    window_height, window_width = screen.getmaxyx() # getting window size
    pos_start_y = (window_height + 6) - window_height
    pos_start_x = (window_width - 1)
    return pos_start_y, pos_start_x

window_height, window_width = get_win_one_res(screen)
pos_start_y, pos_start_x = get_win_two_res(screen)

screen.bkgd(curses.color_pair(yellow_background)) # setting bacground color for first window launch

#----------------------------------------------------------------------------------------------------------#

# curses early stages/messing around
def func():
    #  the first try/except is printing the countdown window when you first launch
    # reason for whie loops is so the window can be rejusted without crashing.
    # *NOTE* cannot shrink below very small size... (idk exact terminal size)
    try:
        count = 0
        while(count != 1000):
            middle_height, middle_width = get_win_one_res(screen)
            screen.clear()
            screen.border()
            screen.addstr(middle_height - 2, middle_width - 22 , '(>0.0)>   -_-_COUNTDOWN HYPE_-_-   <(0.0<)', curses.color_pair(yellow_background))
            screen.addch(middle_height, middle_width - 1, '3', curses.color_pair(yellow_background))
            screen.refresh()
            count += 1

        count1 = 0
        while(count1 != 1000):
            middle_height, middle_width = get_win_one_res(screen)
            screen.clear()
            screen.border()
            screen.addstr(middle_height - 2, middle_width - 22 , '(>0.0)>   -_-_COUNTDOWN HYPE_-_-   <(0.0<)', curses.color_pair(yellow_background))
            screen.addch(middle_height, middle_width - 1, '2', curses.color_pair(yellow_background))
            screen.refresh()
            count1 += 1

        count2 = 0
        while(count2 != 1000):
            middle_height, middle_width = get_win_one_res(screen)
            screen.clear()
            screen.border()
            screen.addstr(middle_height - 2, middle_width - 22 , '(>0.0)>   -_-_COUNTDOWN HYPE_-_-   <(0.0<)', curses.color_pair(yellow_background))
            screen.addch(middle_height, middle_width - 1, '1', curses.color_pair(yellow_background))
            screen.refresh()
            count2 += 1
        count3 = 0
        while(count3 != 1000):
            middle_height, middle_width = get_win_one_res(screen)
            screen.clear()
            screen.border()
            screen.addstr(middle_height - 2, middle_width - 22 , '(>0.0)>   -_-_COUNTDOWN HYPE_-_-   <(0.0<)', curses.color_pair(yellow_background))
            screen.addstr(middle_height, middle_width - 2, 'GO!', curses.color_pair(yellow_background))
            screen.refresh()
            count3 += 1
        screen.clear()
    except KeyboardInterrupt: # for user wanting to ctr ^C
        curses.endwin()
        sys.exit()

    # instations of the donwnloader class and starting threads for the objects
    player1 = dc.Downloader()
    player2 = dc.Downloader()
    player3 = dc.Downloader()
    player4 = dc.Downloader()
    player5 = dc.Downloader()
    player1.set_total_length(url)
    player2.set_total_length(url2)
    player3.set_total_length(url3)
    player4.set_total_length(url4)
    player5.set_total_length(url4)

    thread1 = Thread(target=player1.set_data_length, args=(url,))
    thread2 = Thread(target=player2.set_data_length, args=(url2,))
    thread3 = Thread(target=player3.set_data_length, args=(url3,))
    thread4 = Thread(target=player4.set_data_length, args=(url4,))
    thread5 = Thread(target=player5.set_data_length, args=(url4,))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    screen.bkgd(curses.color_pair(default)) # setting color for the race window

    try:
        loading = '.'
        bool = True
        start_time1 = time.time()
        while(bool == True):
            pos_start_y, pos_start_x = get_win_two_res(screen) # getting window size (testing rn)
            middle_height, middle_width = get_win_one_res(screen)
            window_height, window_width = screen.getmaxyx() # getting window size

            screen.clear() # clearing each for each new frame of print
            screen.border() # displaying border

            # player 1 and player 2 percent for printing
            # player1_percent_done_print is percentage based on window size
            # while player1_done_percent is actual percentage downloaded
            player1_percent_done_print = int((window_width - 23) * player1.data_length/player1.total_length)
            player1_percent_done = int(100 * player1.data_length/player1.total_length)
            player2_percent_done_print = int((window_width - 23) * player2.data_length/player2.total_length)
            player2_percent_done = int(100 * player2.data_length/player2.total_length)
            player3_percent_done_print = int((window_width - 23) * player3.data_length/player3.total_length)
            player3_percent_done = int(100 * player3.data_length/player3.total_length)
            player4_percent_done_print = int((window_width - 23) * player4.data_length/player4.total_length)
            player4_percent_done = int(100 * player4.data_length/player4.total_length)
            player5_percent_done_print = int((window_width - 23) * player5.data_length/player5.total_length)
            player5_percent_done = int(100 * player5.data_length/player5.total_length)
                        # Title for the race window
            screen.addstr(pos_start_y - 4 , middle_width - 13, "WE GONA RACE TODAY COACH", curses.color_pair(blue))
            screen.addstr(pos_start_y - 3, middle_width - 14, '--------------------------', curses.color_pair(blue))

            #player 1
            screen.addstr(6, 2,  "Player1 ::", curses.color_pair(cyan_dots))
            screen.addstr(6, 13, "| Rate: %.3f MBs" % (round(player1.get_data_length()/(time.time()+1 -start_time1)/1024/1024, 3)))
            screen.addstr(6, 31, "| Percent Downloaded: %s%%" % (player1_percent_done))
            screen.addstr(8, 2, "start |%s:]%s| finish!" % ('-' * player1_percent_done_print, ' ' *(pos_start_x - 23 - player1_percent_done_print)), curses.color_pair(yellow_text))
            if(player1_percent_done == 100):
                screen.addstr(6, 21, "0.000", curses.color_pair(red))
                screen.addstr(8, 2, "start |%s:]%s| finish!" % ('-' * player1_percent_done_print, ' ' *(pos_start_x - 23 - player1_percent_done_print)), curses.color_pair(yellow_text))
                winner = player1

            # player 2
            screen.addstr(12, 2, "Player2 ::" , curses.color_pair(cyan_dots))
            screen.addstr(12, 13, "| Rate: %.3f MBs" % (round(player2.get_data_length()/(time.time()+1 - start_time1)/1024/1024, 3)))
            screen.addstr(12, 31, "| Percent Downloaded: %s%%" % (player2_percent_done))
            screen.addstr(14, 2, "start |%s:]%s| finish!" % ('-' * player2_percent_done_print, ' ' *(pos_start_x - 23 - player2_percent_done_print)), curses.color_pair(yellow_text))
            if(player2_percent_done == 100):
                screen.addstr(12, 21, "0.000", curses.color_pair(red))
                screen.addstr(14, 2, "start |%s:]%s| finish!" % ('-' * player2_percent_done_print, ' ' *(pos_start_x - 23 - player2_percent_done_print)), curses.color_pair(yellow_text))
                winner = player2

            # player 3
            screen.addstr(18, 2, "Player3 ::" , curses.color_pair(cyan_dots))
            screen.addstr(18, 13, "| Rate: %.3f MBs" % (round(player3.get_data_length()/(time.time()+1 - start_time1)/1024/1024, 3)))
            screen.addstr(18, 31, "| Percent Downloaded: %s%%" % (player3_percent_done))
            screen.addstr(20, 2, "start |%s:]%s| finish!" % ('-' * player3_percent_done_print, ' ' *(pos_start_x - 23 - player3_percent_done_print)), curses.color_pair(yellow_text))
            if(player3_percent_done == 100):
                screen.addstr(18, 21, "0.000", curses.color_pair(red))
                screen.addstr(20, 2, "start |%s:]%s| finish!" % ('-' * player3_percent_done_print, ' ' *(pos_start_x - 23 - player3_percent_done_print)), curses.color_pair(yellow_text))
                winner = player3

            # player 4
            screen.addstr(24, 2, "Player4 ::" , curses.color_pair(cyan_dots))
            screen.addstr(24, 13, "| Rate: %.3f MBs" % (round(player4.get_data_length()/(time.time()+1 - start_time1)/1024/1024, 3)))
            screen.addstr(24, 31, "| Percent Downloaded: %s%%" % (player4_percent_done))
            screen.addstr(26, 2, "start |%s:]%s| finish!" % ('-' * player4_percent_done_print, ' ' *(pos_start_x - 23 - player4_percent_done_print)), curses.color_pair(yellow_text))
            if(player4_percent_done == 100):
                screen.addstr(24, 21, "0.000", curses.color_pair(red))
                screen.addstr(26, 2, "start |%s:]%s| finish!" % ('-' * player4_percent_done_print, ' ' *(pos_start_x - 23 - player4_percent_done_print)), curses.color_pair(yellow_text))
                winner = player4

            # player 5
            screen.addstr(30, 2, "Player5 ::" , curses.color_pair(cyan_dots))
            screen.addstr(30, 13, "| Rate: %.3f MBs" % (round(player5.get_data_length()/(time.time()+1 - start_time1)/1024/1024, 3)))
            screen.addstr(30, 31, "| Percent Downloaded: %s%%" % (player5_percent_done))
            screen.addstr(32, 2, "start |%s:]%s| finish!" % ('-' * player5_percent_done_print, ' ' *(pos_start_x - 23 - player5_percent_done_print)), curses.color_pair(yellow_text))
            if(player4_percent_done == 100):
                screen.addstr(30, 21, "0.000", curses.color_pair(red))
                screen.addstr(32, 2, "start |%s:]%s| finish!" % ('-' * player5_percent_done_print, ' ' *(pos_start_x - 23 - player5_percent_done_print)), curses.color_pair(yellow_text))
                winner = player5

            '''
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
                    screen.border()
                    screen.refresh()
                    time.sleep(.50)
            '''
            screen.refresh()
            time.sleep(.1)
    except KeyboardInterrupt:
        curses.endwin()
        sys.exit()

func()
