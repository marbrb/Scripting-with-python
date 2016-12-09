#!/usr/bin/python3
#encoding: utf8
import socket
from sys import argv
def bannerGrabbing(host, port):
    "Connect to the port and receive data from this."
    try:
        connection = socket.socket()
        connection.settimeout(1)
        connection.connect((host, port))
        connection.send(b'Exploiter.co')
        result = connection.recv(1024)
        print('[+] {} Abierto :-)'.format(port))
        print(result)

    except:
        print('[-] {} Cerrado :-('.format(port))

    finally:
        connection.close()

ports = [21, 22, 80, 445, 139, 8080]

for port in ports:
    bannerGrabbing(argv[1], port)
