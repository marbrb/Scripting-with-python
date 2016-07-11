#encoding: utf8
import sys
import socket
import threading
import argparse
import requests
from bs4 import BeautifulSoup

def server_loop(lHost, lPort, rHost, rPort,receive_first):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((lHost,lPort))
    except:
        print "[-] Failed to listen on {}:{}".format(lHost,lPort)

        print "[*] Check for other listening sockets or correct permissions."

        sys.exit(0)

    print "[*] Listening on {}:{}".format(lHost, lPort)
    server.listen(5)

    while True:
        client_socket, address = server.accept()
        print "[==>] Received incoming connection from {}:%{}".format(address[0],address[1])

        proxy_thread = threading.Thread(target=proxy_handler, args=(client_socket,rHost,rPort,receive_first))
        proxy_thread.start()

#print out hexadecimal values and ASCII-printable characters
# def hexdump(src, length=16):
#     result = []
#     #great
#     digits = 4 if isinstance(src, unicode) else 2
#
#     for i in xrange(0, len(src), length):
#         s = src[i:i+length]
#         hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
#         text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
#         result.append( b"%04X %-*s %s" % (i, length*(digits + 1), hexa, text))
#
#     print b'\n'.join(result)

def receive_from(connection):
    buffer = ""
    connection.settimeout(3)

    try:
        #keep reading into the buffer until there's no more data or we time out
        while 1:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except:
        pass

    return buffer

#modify any requets destined for the remote host(The server)
def request_handler(buffer):
    print "REQUEST : {}".format(buffer)
    return buffer
    #r = requests.get('http://'+buffer)
    #return r.text.encode('ascii','ignore')

    #soup = BeautifulSoup(r.text.encode('ascii','ignore'), 'html.parser')
    #return str(soup)


#modify any response destined for the local host!
def response_handler(buffer):
    print "RESPONSE : {}".format(buffer)
    #perform packet modifications
    return buffer


def proxy_handler(client_socket, rHost, rPort, receive_first):

    #Socket to connect proxy with the sremote host (the server)
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((rHost, rPort))

    #receive data from the remote end if necessary
    if receive_first:
        remote_buffer = receive_from(remote_socket)
        #hexdump(remote_buffer)

        #send it to our response handler
        remote_buffer = response_handler(remote_buffer)

        # if we have data to send to our local client, send it
        if len(remote_buffer):
            print "[<==] Sending {} bytes to localhost.".format(len(remote_buffer))
            client_socket.send(remote_buffer)
    #read loop and local
    #send to remote, send to local

    while 1:
        #read from local host
        local_buffer = receive_from(client_socket)

        if len(local_buffer):
            print "[==>] Received {} bytes from localhost.".format(len(local_buffer))
        #    hexdump(local_buffer)

            #send it to our local request handler
            local_buffer = request_handler(local_buffer)

            #send off the data to the remote host
            remote_socket.send(local_buffer)
            print "[==>] send to remote {} bytes.".format(len(local_buffer))

        #receive back the response
        remote_buffer = receive_from(remote_socket)

        if len(remote_buffer):
            print "[<==] Received {} bytes from remote.".format(len(remote_buffer))
        #    hexdump(remote_buffer)

            #send to our response handler
            remote_buffer = response_handler(remote_buffer)

            #send the response to the local socket
            client_socket.send(remote_buffer)
            print "[<==] Sent to localhost."

        #if no more data on either side, close the connections
        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()

            print "[*] No more data. Close the connections."
            break






def main():
    parser = argparse.ArgumentParser(description= "TCP Proxy :-)")
    parser.add_argument("-lh", "--localh", dest="lHost", help="type local host", default="localhost")
    parser.add_argument("-lp", "--localp", dest="lPort", help="specify the local port", required=True)
    parser.add_argument("-rh", "--remoteh", dest="rHost", help="specify the remote host", required=True)
    parser.add_argument("-rp", "--remotep", dest="rPort", help="specify the remote port", required=True)
    parser.add_argument("-R", "--receive", dest="receive_first", help="boolean option (True/False)", required=True)
    arguments = parser.parse_args()

    try:
        server_loop(arguments.lHost, int(arguments.lPort), arguments.rHost, int(arguments.rPort), arguments.receive_first)
    except KeyboardInterrupt:
        print "\nCtrl C - Sopping proxy"
        sys.exit(1)

if __name__ == "__main__":
    main()
