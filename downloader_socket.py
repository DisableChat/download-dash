import socket
import time

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
request = "GET /20MB.zip HTTP/1.1\r\nHOST: "+server+"\r\n\r\n" #20971520
#request = "GET /latest/SFTBR-04.PDF HTTP/1.1\r\nHOST: "+server+"\r\n\r\n"
#request = "GET /200MB.zip HTTP/1.1\r\nHOST: "+server+"\r\n\r\n"

# conneting to server
s.connect((server, port))
s.send(request.encode())


# attempting to download from site and break loop when complete.
# hard coding size for now to nice problem solve.
count = 0
bool = True
start_time = time.time()
while(bool == True):
    result = s.recv(4096)
    count += 4096
    #print(result)
    if(count >= 20971520):
        break
end_time = time.time()
print("\n\n", start_time, " ", end_time)
print('\n\n', (end_time - start_time))
