#client_tcp_bc.py

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "172.20.51.255"
port = 2020
message = "hello world!!"
clisock.sendto(message.encode(), (ip, port))
clisock.close();