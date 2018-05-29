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
            for data in response.iter_content(chunk_size = 1024):
                #print(self.data_length)
                self.data_length += len(data)
                f.write(data)
    # setting the total length
    def set_total_length(self, url):
        self.total_length = urllib.request.urlopen(url)
        self.total_length = int(self.total_length.headers['content-length'])
        #print('File Size: ', round(self.total_length/1024/1024, 3), 'MB')

    # Accesor functions
    def get_data_length(self):
        #print("this is the Updated data length")
        return self.data_length

    def get_total_length(self):
        return self.total_length

file_name = "download.data" # declaring name of file in directory
