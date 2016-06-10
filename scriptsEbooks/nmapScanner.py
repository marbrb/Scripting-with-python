#!/usr/bin/python

#Author: Miguel Rodriguez
#Date: 10/07/2016
#Description: Simple port scanner using nmap
#Contact: marbrb1@gmail.com

import nmap
import argparse

def nmapScan(targetHost, targetPort):
    scanner = nmap.PortScanner()
    scanner.scan(targetHost, targetPort)
    state = scanner[targetHost].tcp(int(targetPort))['state']
    print "[*] {} tcp/{} {}".format(targetHost, targetPort, state)

def main():
    parser = argparse.ArgumentParser(description="Simple port scanner using nmap")
    parser.add_argument("-H","--host", dest="targetHost", help="specify target host", required=True)
    parser.add_argument("-p", "--port", dest="targetPort", type=str, help="specify target port(s) separated by comma\nExample: 21,22,80,443", required=True)
    arguments = parser.parse_args()
    for port in arguments.targetPort.split(","):
        nmapScan(arguments.targetHost, port)

if __name__ == "__main__":
    main()
