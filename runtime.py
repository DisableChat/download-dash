# implementation

import downloader_class as dc
import sys
import time
from threading import Thread

##
# Determining file size before download and also downloading file from url
# While also displaying the horse running(downloading animation)
##

url = 'https://www.sample-videos.com/img/Sample-jpg-image-1mb.jpg'
url2 = 'https://www.sample-videos.com/img/Sample-jpg-image-5mb.jpg' # hard coding url from now
url3= 'https://www.sample-videos.com/img/Sample-jpg-image-30mb.jpg'
#file_name = "download.data" # declaring name of file in directory


#attempting to create thread so we can print the player1.data_length()
def main():
    bool = True
    player1 = dc.Downloader()
    player1.set_total_length(url)
    thread1 = Thread(target=player1.set_data_length, args=(url,))
    thread1.start()
    start_time = time.time()
    #player1.set_data_length(url)
    #print(player1.get_data_length())

    while(bool == True):
        #print(player1.get_data_length())
        done = int(50 * player1.data_length / player1.total_length) # done is 50 * data_length divided by total length
        sys.stdout.write("\rRate:   %.3f mbs Percent Downloaded: %s%%  start |%s|:]%s| finish!" %
            (round((player1.data_length/(time.time()- start_time)) /1024/1024, 3), 2*done, '-' * done, ' ' * (50-done)))
        sys.stdout.flush() #makes the terminal output faster by flushing buffer
        #time.sleep(.2)
        if(player1.get_data_length() == player1.get_total_length()):
            #print(player1.get_data_length())
            done = int(50 * player1.data_length / player1.total_length) # done is 50 * data_length divided by total length
            sys.stdout.write("\rRate:   %.3f mbs Percent Downloaded: %s%%  start |%s|:]%s| finish!" %
            (round((player1.data_length/(time.time()- start_time)) /1024/1024, 3), 2*done, '-' * done, ' ' * (50-done)))
            sys.stdout.flush()
            bool = False

    #dc.download_data(url, player1.data_length)

main()
