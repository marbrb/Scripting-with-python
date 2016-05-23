#encoding: utf8
import socket

#retorna la version y que servicio esta corriendo
def bannerGrabbing(host, port):
    try:
        connection = socket.socket()
        connection.settimeout(1)    #tiempo en el que trata de conectarse o recibir una conexion
        connection.connect((host, port))
        connection.send(b'Exploiter.co')
        result = connection.recv(1024)
        print('[+] {} Abierto :-)'.format(port))
        print(result)

    except:
        print('[-] {} Cerrado :-('.format(port))

    finally:
        connection.close()

ports = [21, 22, 80, 445, 139, 8080]

for port in ports:
    bannerGrabbing('192.168.0.18', port) #ip calvo
