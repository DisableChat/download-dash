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
    player1 = dc.Downloader(0, 0)
    player1.set_total_length(url)
    thread1 = Thread(player1.set_data_length(url))
    thread1.start()

    while(player1.get_data_length() != player1.total_length):
        print('HI')

    #dc.download_data(url, player1.data_length)

main()
