#!/usr/bin/python

#Author: Miguel Rodriguez
#Date: 07/07/2016
#Description: UNIX password cracker
#Contact: marbrb1@gmail.com

import zipfile
from threading import Thread
import argparse

parser = argparse.ArgumentParser(description="Zip-File password cracker")

parser.add_argument("-f", "--file", dest="zipfile", help="zip-file path", required=True)

arguments = parser.parse_args()

def extractFile(zipFile, password):
    try:
        zipFile.extractall(pwd=password)
        print "[+] Found password: %s"%(password)
    except:
        pass

def main():
    zipFile = zipfile.ZipFile(arguments.zipfile)
    passFile = open("dictionary.txt", "r")
    for line in passFile.readlines():
        password = line.strip("\n")
        thread = Thread(target=extractFile, args=(zipFile, password))
        thread.start()

if __name__ == "__main__":
    main()
