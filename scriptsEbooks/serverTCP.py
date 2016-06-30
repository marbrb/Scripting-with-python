import socket
import threading
from sys import exit

bindIP = "0.0.0.0"
bindPort = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bindIP, bindPort))

server.listen(5)
print "[*] listening on {}:{}".format(bindIP,bindPort)

def handleClient(clientSocket):
    request = clientSocket.recv(1024)
    print "[*] Recived: " + str(request)

    clientSocket.send("ACK!")   #send back a packet

    clientSocket.close()

while 1:
    try:
        client, addr = server.accept()
        print "[*] Accepted connection from: {}:{}".format(addr[0], addr[1])
        
        handler = threading.Thread(target=handleClient, args=(client,))
        handler.start()
    except KeyboardInterrupt:
        print "\nCtrl C - Stopping server."
        exit(1)        
