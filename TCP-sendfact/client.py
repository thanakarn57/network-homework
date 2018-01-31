#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = input("Pick a number: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(str(MESSAGE))
data = s.recv(BUFFER_SIZE)
s.close()
print "send data:", MESSAGE
print "received data:", data
