import socket;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(5)

host = input(str("Please enter the IP address you want to scan: "))
port = int(input("Please enter the port number you want to scan: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("port is closed,")
    else:
        print("port is open,")
        
portScanner(port)
    

