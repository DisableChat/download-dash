import requests
from urllib import request
import sys
import urllib
##
# Determining file size before download and also downloading file from url
# While also displaying the horse running(downloading animation)
##

url = 'https://www.sample-videos.com/img/Sample-jpg-image-5mb.jpg' # hard coding url from now
url2 = 'https://www.sample-videos.com/img/Sample-jpg-image-1mb.jpg'
file_name = "download.data" # declaring name of file in directory

#printing the size of the file from url
def size_info(url):
    print ("opening url:", url)
    url_size = urllib.request.urlopen(url)
    print('File Size: ', url_size.headers['content-length'], 'bytes') #printing file size


# downloading file and displaying progress
def download_data(url):
    with open(file_name, "wb") as f: #opening file and writing as binary
        print ("Downloading File My Guy and saving as %s" % file_name)
        response = requests.get(url, stream=True) #setting up the requests.get from download url
        total_length = response.headers.get('content-length')
        data_length = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size = 1024):
            data_length += len(data) #  updating data length
            f.write(data) # file write data
            done = int(50 * data_length / total_length) # done is 50 * data_length divided by total length
            #printing the horse running animation
            sys.stdout.write("\rstart |%s|:]%s| finish" % ('-' * done, ' ' * (50-done)))
            sys.stdout.flush() #makes the terminal output faster by flushing buffer

def main(url):
    size_info(url)
    download_data(url)
    print('\n')
main(url)
