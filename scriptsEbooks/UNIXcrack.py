#!/usr/bin/python

#Author: Miguel Rodriguez
#Date: 07/07/2016
#Description: UNIX password cracker
#Contact: marbrb1@gmail.com

import crypt

def testPass(cryptPass):
    salt = cryptPass[:2]
    dictFile = open("dictionary.txt", "r")
    for word in dictFile.readlines():
        word = word.strip("\n")
        cryptWord = crypt.crypt(word, salt)
        if cryptWord == cryptPass:
            print "[+] Found password:  %s\n"%(word)
            return
    print "[-] Password not found.\n"
    return

def main():
    passFile = open("passwords.txt", "r")
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip("\n")
            print "Cracking password for: %s"%(user)
            testPass(cryptPass)

if __name__ == "__main__":
    main()

#TODO: Update the script to crack SHA-512 hashes
