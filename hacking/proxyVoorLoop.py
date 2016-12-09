#!/usr/bin/python
import socket
import select   #Waiting for I/O completion
import time
import sys

#                       TCP PROXY


buffer_size = 4096
delay = 0.0001
forward_to = ('localhost', 8888)

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
    channel = {}    #to associate the endpoints(client<==>server)
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
        forward = Forward().start(forward_to[0], forward_to[1]) #connection with remote server
        clientsock, clientaddr = self.server.accept()   #accept the client connection
        if forward:
            print "{} has connected.".format(clientaddr)
            #added both sockets to input_list
            self.input_list.append(clientsock)
            self.input_list.append(forward)
            #added endpoints to channel dict
            self.channel[clientsock] = forward
            self.channel[forward] = clientsock

        else:
            print "Can't establish connection with remote server."
            print "Closing connection with client side", clientaddr
            clientsock.close()

    def on_close(self):
        print self.s.getpeername(), "has disconnected\n"
        #remove objects from input list
        self.input_list.remove(self.s)
        self.input_list.remove(self.channel[self.s])
        out = self.channel[self.s]
        #close the connection with client
        self.channel[out].close()   #equivalent to do self.s.close()
        #close the connection with remote server
        self.channel[self.s].close()
        #delete both objects from channel dict
        del self.channel[out]
        del self.channel[self.s]

    def on_recv(self):
        data = self.data
        if self.s.getsockname()[1] == 9000:
            print "Client message:  {}".format(data)
        else:
            print "Server message:  {}".format(data)

        self.channel[self.s].send(data)

if __name__ == "__main__":
    server = Server('localhost', 9000)
    try:
        server.main_loop()
    except KeyboardInterrupt:
        print "\nCtrl C - Sopping proxy"
        sys.exit(1)
