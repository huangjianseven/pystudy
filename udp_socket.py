import socket

s = socket.socket(socket.AF_INET,SOCK_DGRAM)

s.bind('192.168.3.13',8088)
