#encoding: utf8
import socket
from sys import argv

def portScan(host, port):
    try:
        connection = socket.socket()
        connection.settimeout(1)    #tiempo de conexion
        connection.connect((host, port))    #trata de conectarse
        connection.send(b'Exploiter.co')    #enviar algo en bytes para ver si el puerto responde
        print("{}/tpc ABIERTO :-D".format(port))
    except:
        print("{}/tpc CERRADO :-(".format(port))
    finally:
        connection.close()

ports = [21, 22, 80, 445, 139, 8080]

for port in ports:
    portScan(argv[1], port)
