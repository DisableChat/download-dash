import requests
import sys
import urllib
import time
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
    file_size = int(url_size.headers['content-length'])
    print('File Size: ', round(file_size/1048576, 2), 'mb')
    print('File Size: ', url_size.headers['content-length'], 'bytes') #printing file size

# this will probably be implemented after multithreading is implemented.
'''
def percent_downloaded(url):
    with open(file_name, "wb") as f: #opening file and writing as binary
        print ("Downloading File My Guy and saving as %s" % file_name)
        response = requests.get(url, stream=True) #setting up the requests.get from download url
        total_length = response.headers.get('content-length')
        data_length = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size = 1024):
            data_length += len(data) #  updating data length
            f.write(data) # file write data
            done = int(100 * data_length / total_length) # done is 50 * data_length divided by total length
            #printing the horse running animation
            sys.stdout.write('\rPercent Downloaded %s %%' % (done))
            sys.stdout.flush() #makes the terminal output faster by flushing buffer
'''

# downloading file and displaying progress
def download_data(url):
    with open(file_name, "wb") as f: #opening file and writing as binary
        print ("Downloading File My Guy and saving as %s" % file_name)
        response = requests.get(url, stream=True) #setting up the requests.get from download url
        total_length = response.headers.get('content-length')
        data_length = 0
        total_length = int(total_length)
        start_time = time.time()
        for data in response.iter_content(chunk_size = 1024):
            data_length += len(data) #  updating data length
            f.write(data) # file write data
            done = int(50 * data_length / total_length) # done is 50 * data_length divided by total length
            #printing the horse running animation also displays download rate and percent_downloaded
            sys.stdout.write("\rRate:   %.3f mbs Percent Downloaded: %s%%  start |%s|:]%s| finish!" %
                (round((data_length/(time.time()- start_time)) /1024/1024, 3), 2*done, '-' * done, ' ' * (50-done)))
            sys.stdout.flush() #makes the terminal output faster by flushing buffer

def main(url):
    size_info(url)
    download_data(url)
    print('\n')
main(url)
