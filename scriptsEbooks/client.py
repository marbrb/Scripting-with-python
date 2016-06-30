import socket
import sys
host = sys.argv[0]
port = sys.argv[1]
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((host, port))
except Exception as e:
    print "Error {}".format(e)

client.send("rsdaaddasdadadasdasas\n\r\n")

response = client.recv(1024)
client.close()
print response

