#sockets initialize connections, and send and receive data.
#technical term = socket is an internal endpoint for sending or receiving data on a network.
#socket is like an outlet that gives you power from transformer to house or office. cannot send power thru socket

import socket #import socket module
#creating the sockey object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket object
#AF_INET = address family, IPv4, TCP protocol

#store the hostname 
#host = '10.169.165.244'
host = socket.gethostname() #get host name

port = 444 #reserve a port for your service


#binding to socket
# bind to the port; host will be replaced/substituted by IP address
server_socket.bind(('10.169.160.1', port))

#start to listen for TCP connections from client
server_socket.listen(3) #3 = number of requests that can be allowed at a given time 

while True:
    #starting the connection
    client_socket, address = server_socket.accept() #allow TCP connection information from client
    
    print("received connection from %s" % str(address))
    
    message = "Thank you for connecting to the server " + "\r\n"
    client_socket.send(message.encode('ascii')) #send message to client
    
    
    client_socket.close() #close the connection

