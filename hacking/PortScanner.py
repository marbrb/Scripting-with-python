#!/usr/bin/python

#Author: Miguel Rodriguez
#Date: 09/06/2016
#Description: Port Scanner
#Contact: marbrb1@gmail.com

import argparse
import socket
from threading import Thread, Semaphore
from socket import *

screenlock = Semaphore(value=1)
def connScan(targetHost, targetPort):
    try:
        conSocket = socket(AF_INET, SOCK_STREAM)    #(IPV4, TCP)
        conSocket.connect((targetHost, targetPort))
        conSocket.send('ViolentPython\r\n')
        response = conSocket.recv(100)
        screenlock.acquire()
        print "[+] %d/tcp open"% targetPort
        if response:
            print "[+] response: "+ str(response)
        conSocket.close()

    except:
        screenlock.acquire()
        print "[-] %d/tcp closed"% targetPort

    finally:
        screenlock.release()
        conSocket.close()


def portScan(targetHost, targetPorts):
    try:
        targetIP = gethostbyname(targetHost)

    except:
        print "[-] Cannot resolve '%s': Unknow host"% targetHost
        return

    try:
        targetName = hostbyaddr(targetIP)
        print "\nScan results for: " + targetName[0]

    except:
        print "\nScan results for: " + targetIP

    setdefaulttimeout(1)

    for port in targetPorts:
        t = Thread(target=connScan, args=(targetHost, int(port)))
        t.start()

def main():
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("-H", "--host", dest="targetHost", help="Type the target host", required=True)
    parser.add_argument("-p", "--port", dest="targetPort", type=str, help="Type the target port", required=True)
    arguments = parser.parse_args()

    targetPorts = arguments.targetPort.split(",")
    portScan(arguments.targetHost, targetPorts)

if __name__ == "__main__":
    main()
