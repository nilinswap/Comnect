import socket
import sys, datetime

udp_ip_address = "172.172.172.172"
udp_port_no = 2020
message = "hello, server"

clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientsock.sendto(message.encode(), (udp_ip_address, udp_port_no))

