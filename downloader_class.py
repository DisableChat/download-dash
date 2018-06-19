import requests
import sys
import time
import urllib
import socket
from threading import Thread

##
# Downloader class is a class for the "Players" used in the race. This includes
# all the neccary vars and functions needed by the runtime.py
##

timing_array    = []

class Downloader:

    # Players data_length and total_length and percent done
    data_length     = 0
    total_length    = 1
    percent_done    = 0

    # Average download and peak download var
    overall_average_download    = 0
    peak_download               = 0
    peak_download_high          = 0

    # Flags used
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

    # Used for each player time end var
    time_end = 0

    # Runs threads while true, else quit player threads
    run_thread      = True
    url_array_os    = []

    # Rankings
    ranking_array   = []
    #timing_array    = []
    #ranking_array   = ['','','','','','']

    def __init__(self):

        index = 0

    # Deterimines if there is a redirect error (301 ERROR), if it does occur find new route
    def determine_error(self, s):

        if(self.header.find('404 Not Found' or 'Not Found' or 'Service Unavailable' or '302 Found' or '403 Forbidden') != -1):

            # Hard coded url for now incase of error thats not a 301 rederect
            url_redirect = 'http://repos-jnb.psychz.net/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-1804.iso'
            server, directories = self.parse_server_info(url_redirect)
            request = "GET "+directories+" HTTP/1.1\r\nHOST: "+server+"\r\n\r\n"

            # closing old socket and then creating new one to download from
            s.shutdown(1)
            s.close()
            d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            d.connect((server, 80))
            d.send(request.encode())

            new_header = d.recv(4096)
            new_header = str(new_header)
            self.header = new_header

            self.parse_content_length()
            self.data_length += len(self.header)

            # Receiving stream of packets
            while(self.run_thread):
                result = d.recv(4096)
                self.data_length += len(result)
                self.chunk += len(result)
                self.set_chunk_rate()
                if(self.data_length == self.total_length):
                    break

        elif(self.header.find('301 Moved Permanently') != -1):

            url_redirect = ''

            pos = self.header.find('Location:') + 11
            for i in range(pos, 1024 - pos, 1):
                url_redirect += self.header[i - 1]
                if(self.header[i] == "\\"):
                    break

            url_redirect = ''.join(url_redirect)
            server, directories = self.parse_server_info(url_redirect)
            request = "GET "+directories+" HTTP/1.1\r\nHOST: "+server+"\r\n\r\n"

            s.send(request.encode())

            new_header = s.recv(4096)
            new_header = str(new_header)
            self.header = new_header

        else:
            return

    # Parses server address as well as download directories
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

    # Function used to parse out the content length from http header
    def parse_content_length(self):
        content_length = ''
        content_length_pos = self.header.find('Content-Length') + 17
        for i in range(content_length_pos, 4096 - content_length_pos, 1):
            content_length += self.header[i - 1]
            if(self.header[i] == "\\"):
                break
        self.total_length = int(content_length)

    def download(self, url, url_array_os, index):
        self.index = index
        self.url_array_os = url_array_os
        # Setting up socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            sys.exit("Socket Error %s" %(err))

        # Setting Url, Port, Server, and Directory and request info
        self.url = url
        port = 80
        server, directories = self.parse_server_info(self.url)
        request = "GET "+directories+" HTTP/1.1\r\nHOST: "+server+"\r\n\r\n"

        # Connect To host Try
        try:
            server_ip = socket.gethostbyname(server)
        except socket.gaierror:
            sys.exit("there was an error resolving the host")

        # Conneting to server
        s.connect((server, port))
        s.send(request.encode())

        # recieving header to find out size of download
        self.header = s.recv(4096)
        self.header = str(self.header)
        self.determine_error(s)
        self.parse_content_length()
        self.data_length += len(self.header)

        # Starting timer
        self.chunk_timer_start = time.time()

        # Receiving stream of packets
        while(self.run_thread):
            result = s.recv(4096)
            self.data_length += len(result)
            self.chunk += len(result)
            self.set_chunk_rate()
            if(self.data_length == self.total_length):
                break

    # Determines the chunk rate
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

# converts time from ms to minutes seconds and milliseconds
def get_time(milliseconds):
    ms = milliseconds
    s, ms = divmod(ms, 1000)
    m, s = divmod(s, 60)
    new_time = ('%d:%d:%d'%(m,s, ms))
    return new_time
