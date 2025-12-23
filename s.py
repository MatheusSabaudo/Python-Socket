#!/bin/python3

#SIMPLE PYTHON SOCKET

import socket

HOST = '127.0.0.1' # change you IP here
PORT = 7777 # change your source port here

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # af_inet = ipv4 | sock_stream = port

conn.connect((HOST, PORT))
