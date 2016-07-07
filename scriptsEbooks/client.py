import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((host, port))
    
except Exception as e:
    print "Error {}".format(e)

client.send("Buena el server")

response = client.recv(1024)
client.close()
print "Server reponse:  {}".format(response)


