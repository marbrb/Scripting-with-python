#!/usr/bin/python

#Author: Miguel Rodriguez
#Date: 09/07/2016
#Description: Port Scanner
#Contact: marbrb1@gmail.com

import argparse
import socket
from socket import *

parser = argparse.ArgumentParser(description="Port Scanner")
parser.add_argument("-H", "--host", dest="targetHost", help="Type the target host", required=True)
parser.add_argument("-p", "--port", dest="targetPort", type=str, help="Type the target port", required=True)
arguments = parser.parse_args()

def connScan(targetHost, targetPort):
    try:
        conSocket = socket(AF_INET, SOCK_STREAM)    #(IPV4, TCP)
        conSocket.connect((targetHost, targetPort))
        conSocket.send('ViolentPython\r\n')
        response = conSocket.recv(100)
        print "[+] %d/tcp open"% targetPort
        if response:
            print "[+] response: "+ str(response)
        conSocket.close()

    except:
        print "[-] %d/tcp closed"% targetPort

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
        print "Scannig port "+ port
        connScan(targetHost, int(port))

def main():
    targetPorts = arguments.targetPort.split(",")
    portScan(arguments.targetHost, targetPorts)

if __name__ == "__main__":
    main()
