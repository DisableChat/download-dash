# Downloader Struct
import requests
import sys
import time
import urllib
from threading import Thread

class Downloader:

    # variables needed for class
    data_length = 0
    total_length = 0
    overall_average_download = 0
    peek_download = 0
    peek_download_high = 0
    percent_done = 0

    url = ''

    # getting the percent currently done
    def get_percent_done(self):
        self.percent_done = int(100 * self.data_length/self.total_length)
        return self.percent_done

    # Downloading the length
    def download(self, url):
        with open(file_name, 'wb') as f:
            response = requests.get(url, stream = True)
            for data in response.iter_content(chunk_size = 1024):
                self.data_length += len(data)
                f.write(data)

    # setting the total length
    def set_total_length(self, url):
        self.total_length = urllib.request.urlopen(url)
        self.total_length = int(self.total_length.headers['content-length'])

    # Accesor functions
    def get_data_length(self):
        return self.data_length

    def get_total_length(self):
        return self.total_length

file_name = "download.data" # declaring name of file in directory
