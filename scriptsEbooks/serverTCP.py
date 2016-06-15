import socket
import threading

bindIP = "0.0.0.0"
bindPort = 9999

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
    client, addr = server.accept()
    print "[*] Accepted connection from: {}:{}".format(addr[0], addr[1])

    handler = threading.Thread(target=handleClient, args=(client,))
    handler.start()
