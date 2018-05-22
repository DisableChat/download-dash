# Downloader Struct
import requests
import sys
import time
import urllib
from threading import Thread

class Downloader:
    data_length = 0
    total_length = 0

    # Downloading the length
    def set_data_length(self, url):
        with open(file_name, 'wb') as f:
            response = requests.get(url, stream = True)
            self.total_length = int(self.total_length)
            start_time = time.time()
            for data in response.iter_content(chunk_size = 1024):
                self.data_length += len(data)
                #print(self.data_length)
                f.write(data)

    # setting the total length
    def set_total_length(self, url):
        self.total_length = urllib.request.urlopen(url)
        self.total_length = int(self.total_length.headers['content-length'])
        print('File Size: ', round(self.total_length/1048576, 2), 'mb')

    # Accesor functions
    def get_data_length(self):
        #print("this is the Updated data length")
        return self.data_length

    def get_total_length(self):
        return self.total_length

file_name = "download.data" # declaring name of file in directory

# the following two functions were older implementations from prev ver
def size_info(url):
    print ("opening url:", url)
    url_size = urllib.request.urlopen(url)

    file_size = int(url_size.headers['content-length'])
    total_length = file_size
    print('File Size: ', round(file_size/1048576, 2), 'mb')
    print('File Size: ', url_size.headers['content-length'], 'bytes') #printing file size
    return total_length

def download_data(url, data_length):
    with open(file_name, "wb") as f:
        print ("Downloading File My Guy and saving as %s" % file_name)
        response = requests.get(url, stream = True)
        total_length = response.headers.get('content-length')
        data_length = 0
        total_length = int(total_length)
        start_time = time.time()
        for data in response.iter_content(chunk_size = 1024):
            data_length += len(data)
            f.write(data)
            done = int(50 * data_length / total_length) # done is 50 * data_length divided by total length
            sys.stdout.write("\rRate:   %.3f mbs Percent Downloaded: %s%%  start |%s|:]%s| finish!" %
                (round((data_length/(time.time()- start_time)) /1024/1024, 3), 2*done, '-' * done, ' ' * (50-done)))
            sys.stdout.flush() #makes the terminal output faster by flushing buffer
