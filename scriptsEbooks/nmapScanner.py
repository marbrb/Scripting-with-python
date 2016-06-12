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
    for host in scanner.all_hosts():
        if "tcp" in scanner[host].keys():
            for port in scanner[host]["tcp"].keys().sort():
                print "[*] {} tcp/{} {}".format(host, port, scanner[host].tcp(port)["state"])
            print "\n"

def main():
    parser = argparse.ArgumentParser(description="Simple port scanner using nmap")
    parser.add_argument("-H","--host", dest="targetHost", help="specify target host", required=True)
    parser.add_argument("-p", "--port", dest="targetPort", type=str, help="specify target port(s)", required=True)
    arguments = parser.parse_args()
    nmapScan(arguments.targetHost, arguments.targetPort)

if __name__ == "__main__":
    main()

#TODO: accept more hosts
