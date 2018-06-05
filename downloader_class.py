# Downloader Struct
import requests
import sys
import time
import urllib
import socket
from threading import Thread

class Downloader:

    # Players data_length and total_length and percent done
    data_length     = 0
    total_length    = 1
    percent_done    = 0

    # average download and peak download var
    overall_average_download    = 0
    peak_download               = 0
    peak_download_high          = 0

    #flags used
    done_flag       = False
    stop_avg_flag   = False

    # Used for data download rate arithmitic
    chunk_rate          = 0
    chunk               = 0
    chunk_timer_start   = 0
    chunk_timer_end     = 0


    # String variables for header and url info
    header  = ''
    url     = ''

    #used for each player time end var
    time_end = 0

    #parses server address as well as download directories
    def parse_server_info(self, url):
        url = str(url)
        http_array = list(url)
        if(http_array[0:7] == ['h', 't', 't', 'p', ':', '/', '/']):
            http_array = http_array[7:len(url)]
            url = ''.join(http_array)
            directory_loc_begin = url.find('/')
            server = http_array[0:directory_loc_begin]
            server = ''.join(server)
            directories = http_array[directory_loc_begin:len(url)]
            directories = ''.join(directories)
            return server , directories

    # function used to parse out the content length from http header
    def parse_content_length(self):
        content_length = ''
        content_length_pos = self.header.find('Content-Length') + 17
        for i in range(content_length_pos, 4096 - content_length_pos, 1):
            content_length += self.header[i - 1]
            if(self.header[i] == "\\"):
                break
        self.total_length = int(content_length)
        #return content_length

    def download(self, url):

        # setting up socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket succesfully created
        except socket.error as err:
            sys.exit("Socket Error %s" %(err))

        self.url = url
        port = 80
        server, directories = self.parse_server_info(self.url)
        request = "GET "+directories+" HTTP/1.1\r\nHOST: "+server+"\r\n\r\n"

        try:
            server_ip = socket.gethostbyname(server)
        except socket.gaierror:
            sys.exit("there was an error resolving the host")#could not resolve the host

        # conneting to server
        s.connect((server, port))
        s.send(request.encode())

        self.header = s.recv(4096)
        self.data_length += len(self.header)
        self.header = str(self.header)
        self.parse_content_length()


        self.chunk_timer_start = time.time() #starting timer
        #receving stream of packets
        while(True):
            result = s.recv(4096)
            self.data_length += len(result)
            self.chunk += len(result)
            self.set_chunk_rate()
            if(self.data_length == self.total_length):
                break

    # determines the chunk rate
    def set_chunk_rate(self):
        if((time.time() - self.chunk_timer_start) >= 1):
            self.chunk_rate = self.chunk/(time.time() - self.chunk_timer_start)
            self.chunk_timer_start = time.time()
            self.chunk = 0


    # Accesor functions
    def get_data_length(self):
        return self.data_length

    def get_total_length(self):
        return self.total_length

    def get_percent_done(self):
        self.percent_done = int(100 * self.data_length/self.total_length)
        return self.percent_done
