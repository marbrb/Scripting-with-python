import socket
import threading
import sys

bindIP = sys.argv[1]
bindPort = int(sys.argv[2])
clients = []
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

        clients.append(client)

        handler = threading.Thread(target=handleClient, args=(client,))
        handler.start()
    except KeyboardInterrupt:
        print "\nCtrl C - Stopping server."
        sys.exit(1)
