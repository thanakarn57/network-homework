#!/usr/bin/env python

import socket
import os


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))


path = "./image_from_client/"
fileName = 'superman.jpg'

if not os.path.exists(path):
    os.makedirs(path)
    
s.listen(1)
conn, addr = s.accept()
fileOpen = open(path+fileName,'wb')
print 'Connect address:', addr
data = conn.recv(BUFFER_SIZE)
while data:
    fileOpen.write(data)
    data = conn.recv(BUFFER_SIZE)
fileOpen.close()
print "success receiving"
conn.close()
