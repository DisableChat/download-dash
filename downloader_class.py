# Downloader Struct
import requests
import sys
import time
import urllib
import socket
from threading import Thread

class Downloader:

    # variables needed for class
    data_length = 0
    total_length = 1
    overall_average_download = 0
    peek_download = 0
    peek_download_high = 0
    percent_done = 0
    header = ''
    time_end = 0
    done_flag = False
    stop_avg_flag = False
    url = ''

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

    # getting the percent currently done
    def get_percent_done(self):
        self.percent_done = int(100 * self.data_length/self.total_length)
        return self.percent_done

    def download(self, url):
        # setting up socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #print("Socket succesfully created")
        except socket.error as err:
            sys.exit()
            #print("Socket Error %s" %(err))


        self.url = url
        port = 80
        server, directories = self.parse_server_info(self.url)
        request = "GET "+directories+" HTTP/1.1\r\nHOST: "+server+"\r\n\r\n"

        try:
            server_ip = socket.gethostbyname(server)
            #print(server_ip)
        except socket.gaierror:
            #could not resolve the host
            sys.exit()
            #print("there was an error resolving the host")
            sys.exit()

        # conneting to server
        s.connect((server, port))
        s.send(request.encode())

        self.header = s.recv(4096)
        self.data_length += len(self.header)
        self.header = str(self.header)
        self.parse_content_length()

        while(True):
            result = s.recv(4096)
            self.data_length += len(result)
            if(self.data_length == self.total_length):
                break

    # Accesor functions
    def get_data_length(self):
        return self.data_length

    def get_total_length(self):
        return self.total_length
