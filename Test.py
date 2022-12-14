import socket
from contextlib import closing

host = socket.gethostname()  # get host name
ip_address = socket.gethostbyname(host)
print(host)
print(ip_address)


def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]

find_free_port()