#!/usr/bin/python
import socket
import select   #Waiting for I/O completion
import time
import sys

#                       TCP PROXY


buffer_size = 4096
delay = 0.0001
forward_to = ('0.0.0.0', 8888)

#responsible for establishing a connection between the proxy
#and the remote server(original target).
class Forward:
    def __init__(self):
        self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, host, port):
        try:
            self.forward.connect((host,port))
            return self.forward
        except Exception as e:
            print e
            return False

class Server:
    input_list = [] #storage all the avalible sockets
    channel = {}
    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #prevents TIME_WAIT state of the socket
        self.server.bind((host, port))
        self.server.listen(200)


    def main_loop(self):
        self.input_list.append(self.server)
        while 1:
            time.sleep(delay)
            ss = select.select  #The return value is a triple of lists of objects that are ready: subsets of the first three arguments.
            inputready, outputready, exceptready = ss(self.input_list, [], []) #it's like a filter
            for self.s in inputready:
                if self.s == self.server:
                    self.on_accept()
                    break
                self.data = self.s.recv(buffer_size)
                if len(self.data) == 0:
                    self.on_close()
                    break

                else:
                    self.on_recv()
    def on_accept(self):
        forward = Forward().start(forward_to[0], forward_to[1])
        clientsock, clientaddr = self.server.accept()
        if forward:
            print clientaddr + "{} has connected.".format(clientaddr)
            self.input_list.append(clientsock)
            self.input_list.append(forward)
            self.channel[clientsock] = forward
            self.channel[forward] = clientsock

        else:
            print "Can't establish connection with remote server.",
            print "Closing connection with client side", clientaddr
            clientsock.close()

    def on_recv(self):
        data = self.data
        print data
        self.channel[self.s].send(data)

if __name__ == "__main__":
    server = Server('', 9000)
    try:
        server.main_loop()
    except KeyboardInterrupt:
        print "Ctrl C - Sopping server"
        sys.exit(1)
