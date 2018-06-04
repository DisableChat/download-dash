import socket
import time
import string

# function used to parse out the content length from http header
def parse_content_length(string):
    content_length = ''
    content_length_pos = string.find('Content-Length') + 17
    for i in range(content_length_pos, 4096 - content_length_pos, 1):
        content_length += string[i - 1]
        if(string[i] == "\\"):
            break
    content_length = int(content_length)
    return content_length

# setting up socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket succesfully created")
except socket.error as err:
    print("Socket Error %s" %(err))


#hard coding servers for now.
#server = '212.183.159.230'
server = 'ipv4.download.thinkbroadband.com'
#server = 'ipv4.download.thinkbroadband.com'
#server = 'www.office.xerox.com' # /latest/SFTBR-04.PDF

port = 80

try:
    server_ip = socket.gethostbyname(server)
    print(server_ip)
except socket.gaierror:
    #could not resolve the host
    print("there was an error resolving the host")
    sys.exit()



# messing with the requests by hard coding for now
#request = "GET /100MB.zip HTTP/1.1\r\nHOST: "+server+"\r\n\r\n" #20971520 #NOTE abou 11s download time
#request = "GET /latest/SFTBR-04.PDF HTTP/1.1\r\nHOST: "+server+"\r\n\r\n"
request = "GET /20MB.zip HTTP/1.1\r\nHOST: "+server+"\r\n\r\n" #NOTE about 4 sec download time

# conneting to server
s.connect((server, port))
s.send(request.encode())

var = s.recv(4096)
var = str(var)
#print(var)
content_length = parse_content_length(var)

# attempting to download from site and break loop when complete.
# hard coding size for now to nice problem solve.
count = 0
bool = True
start_time = time.time()
while(bool == True):
    result = s.recv(4096)
    count += 4096
    #sprint(result)
    if(count >= content_length):
        break
end_time = time.time()
print("\n\n", start_time, " ", end_time)
print('\n\n', (end_time - start_time))
