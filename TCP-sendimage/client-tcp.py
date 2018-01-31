#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
fileName = "superman.jpg"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print "picture:", fileName
fileOpen = open(fileName,'rb')
data = fileOpen.read(BUFFER_SIZE)
while (data):
    s.send(data)
    data = fileOpen.read(BUFFER_SIZE)
fileOpen.close()
print "success sending"
s.close()

    

