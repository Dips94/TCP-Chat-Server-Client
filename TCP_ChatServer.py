#import all libraries

import socket
import select
import sys
from thread import *


 # Create a TCP socket
 # Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connections = []
# Assign IP address and port number to socket
serverSocket.bind(('localhost', 14002))
#start to listen for connections
serverSocket.listen(4)	
	
#function to perform the required  	 
def check(conn,addr):	  
  conn.send("This is the chat room")
  while True:
	#receive data from clients
	data = conn.recv(2048)
	data = data.strip()
	#If message is BYE send the message to the other clients and removes the connection
        if data == 'BYE':
	  print data
	  broadcast(data, conn)
	  remove(conn)
	  break
	  #Else send the message to the other clients including their address
	else:
          print data
	  message = "<" + addr[0] + "> " + data
	  print message
	  broadcast(message, conn)
#Broadcast function to send message to all other clients
def broadcast(message, connection):
  for clients in connections:
    if clients!=connection:
      try:
        clients.send(message)
      except:
        clients.close()
        # if the link is broken, we remove the client
        remove(clients)
#To remove the connection
def remove(connection):
  if connection in connections:
    connections.remove(connection)

while True:   
  conn,addr = serverSocket.accept()
 #store the connection in an array 
  connections.append(conn)
  #Starting the thread
  start_new_thread(check,(conn,addr)) 	


conn.close()
serverSocket.close()
 
   		       
