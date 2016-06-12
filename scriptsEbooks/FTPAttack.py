#!/usr/bin/python

#Author: Miguel Rodriguez
#Date: 10/06/2016
#Description: try anonymous logon and dictionary attack to gain access.
#search for default web pages. For each of these pages,
#download a copy and adds a malicious redirection.
#upload the infected page back to the FTP server
#Contact: marbrb1@gmail.com

import ftplib
import argparse
import time

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)  # FTP client
        ftp.login("anonymous", "me@anything.com")
        print "[*] {} FTP anonymous logon succeeded".format(hostname)
        ftp.quit()
        return True

    except:
        print "[*] {} FTP anonymous logon failed".format(hostname)
        return False

def bruteLogin(hostname, passFile):
    pass

def defaultPages(ftp):  # take a FTP connection as argument
    pass

def injectPage(ftp, page, redirect):
    pass

def attack(username, password, targetHost, redirect):
    pass

def main():
    pass

if __name__ == "__main__":
    main()
