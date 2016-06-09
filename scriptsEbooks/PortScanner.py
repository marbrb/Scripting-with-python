#!/usr/bin/python

#Author: Miguel Rodriguez
#Date: 09/07/2016
#Description: Port Scanner
#Contact: marbrb1@gmail.com

import argparse
from socket import *

parser = argparse.ArgumentParser(description="Port Scanner")
parser.add_argument("-p", "--port", dest="targetPort", help="Type the target port", required=True)
parser.add_argument("-h", "--host", dest="targetHost", help="Type the target host", required=True)
arguments = parser.parse_args()

def connScan(targetHost, targetPort):
    try:
        conSocket = socket(AF_INET, SOCK_STREAM)    #(IPV4, TCP)
        conSocket.connect((targetHost, targetPort))
        print "[+] %d/tcp open"% targetPort

    except:
        print "[-] %d/tcp closed"% targetPort

def portScan(targetHost, targetPorts):
    try:
        targetIP = gethostbyname(targetHost)

    except:
        print "[-] Cannot resolve '%s': Unknow host"% targetHost

    try:
        targetName = hostbyaddr(targetIP)
        print "Scan results for: " + targetName[0]

    except:
        print "Scan results for: " + targetIP

    setdefaulttimeout(1)

    for port in targetPorts:
        print "Scannig port "+ port
        connScan(targetHost, int(port))
