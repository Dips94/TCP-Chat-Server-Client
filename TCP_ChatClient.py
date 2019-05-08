#import all libraries

import socket
import select
import sys
 
#initialising all the variables
TCP_IP = '127.0.0.1'
TCP_PORT = 14002
BUFFER_SIZE = 1024
#name = raw_input("Name of client ")
#name_User = raw_input("Name of User")
Message = "Client Y: BOB " # + name + " :" + name_User
# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets 
clientSokcet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connecting to the server
clientSokcet.connect((TCP_IP, TCP_PORT))

while True:
 # maintains a list of possible input streams
    sockets_list = [sys.stdin, clientSokcet]
  #Select returns from sockets_list, the stream that
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

    for socks in read_sockets:
        if socks == clientSokcet:
            message = socks.recv(2048)
            print message
	    message = message.strip()
	    if message == 'BYE':
	       break
        else:
            message = sys.stdin.readline()
            clientSokcet.send(message)
	    message = message.strip()
	    if(message == 'BYE'):
	      break

clientSokcet.close()
