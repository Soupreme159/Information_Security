from http import client
import socket;

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '10.169.165.244'
host = socket.gethostname()

port = 444

clientsocket.connect(('10.169.160.1', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
