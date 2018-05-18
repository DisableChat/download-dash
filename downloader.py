import requests
from urllib import request

##
# Determining file size before download and also downloading file from url
# *note* this basic implementation to pull from url and also determine file
# size pre download
##

url = 'http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv' # hard coding url from now

def size_info(url):
    resp = requests.get(url)
    print('Size Pre Download (recorded) :  ', resp.headers['content-length']) # Size of file pulled from url
    print('Actual size of the file bytes:   123,637') # Size of the file from inspecting from local directory

def download_data(url):
    response = request.urlopen(url)
    file = response.read()
    file = str(file)
    lines = file.split("\\n")
    destination_url = r'links.csv' # raw format of file
    fx = open(destination_url, 'w')
    for line in lines:
        fx.write(line + "\n")
        print('Downloaded and Created a file in directory...')
    fx.close()


def main():
    size_info(url)
    download_data(url)


main()
