#!/usr/bin/python3
# -*- coding: utf-8 -*-

# zmq_SUB_proc.py
# Author: Marc Lichtman

import zmq
import numpy as np
import time
import cv2

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:55555") # connect, not bind, the PUB will bind, only 1 can bind
socket.setsockopt(zmq.SUBSCRIBE, b'') # subscribe to topic of all (needed or else it won't work)



length=1000
width=35
img = np.zeros((width,length))
for i in range(width):
	for j in range(length):
		img[i,j] = 255
cv2.startWindowThread()

stream=''
l=0
while True:
    if socket.poll(10) != 0: # check if there is a message on the socket
        msg = socket.recv() # grab the message
        data = np.frombuffer(msg, dtype=np.uint8, count=-1) # make sure to use correct data type (complex64 or float32); '-1' means read all data in the buffer
        stream+=str(data[0])
        cv2.waitKey(1)
        cv2.imshow('',img)
        if len(stream)>=14:
            for j in range(0,14): #lignes  
	            img[j,l] = (1-float(stream[j]))*255
	            img[j+14,l] = (1-float(stream[j]))*255
	            img[j+1,l+1] = (1-float(stream[j]))*255
	            img[j+14+1,l+1] = (1-float(stream[j]))*255
	            img[j+1,l] = (1-float(stream[j]))*255
	            img[j+14+1,l] = (1-float(stream[j]))*255
	            img[j,l+1] = (1-float(stream[j]))*255
	            img[j+14,l+1] = (1-float(stream[j]))*255
            stream=stream[14:]
            l=l+2
        if l==length-30:
            l=0
            for p in range(width):
                for q in range(length):
                    img[p,q] = 255
    else:
        time.sleep(0.1) # wait 100ms and try again

