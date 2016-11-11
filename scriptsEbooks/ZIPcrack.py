#!/usr/bin/python

#Author: Miguel Rodriguez
#Date: 07/06/2016
#Description: ZIP password cracker
#Contact: marbrb1@gmail.com

import zipfile
from threading import Thread
import argparse

def extractFile(zipFile, password):
    try:
        zipFile.extractall(pwd=password)
        print( "[+] Found password: {}".format(password))
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Zip-File password cracker")
    parser.add_argument("-f", "--file", dest="zipfile", help="zip-file path", required=True)
    arguments = parser.parse_args()

    zipFile = zipfile.ZipFile(arguments.zipfile)
    passFile = open("dictionary.txt", "r")
    for line in passFile.readlines():
        password = line.strip("\n")
        thread = Thread(target=extractFile, args=(zipFile, password))
        thread.start()

if __name__ == "__main__":
    main()
