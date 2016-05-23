#encoding: utf8
import socket
import sys

#script para detectar maquinas que esten ejecutando servicios vulnerables

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#socket IPV4 con protocolo TCP

#recorrer direcciones IP con una lista de puertos
ports = [20,21,22,80,445]
vulnbanners = "lista de banners vulnerables"
for host in range(12, 14):
	#ports = open('ports.txt', 'r')
	#vulnbanners = open('vulnbanners.txt', 'r')
	for port in ports:
		try:
			#sys.argv captura datos que ingrese el usuario por consola al ejecutar el script()posiciones separadas por espacio
			#el usuario debe ingresar un fragmento de red por consola
			socket.connect(( str(sys.argv[1]+'.'+str(host)), int(port) ))	#conexion
			print ('Connecting to '+str(sys.argv[1]+'.'+str(host))+' in the port: '+str(port))
			socket.settimeout(1)
			banner = socket.recv(1024)
			for vulnbanner in vulnbanners:
				if banner.strip() in vulnbanner.strip():
					print ('We have a winner! '+banner)
					print ('Host: '+str(sys.argv[1]+'.'+str(host)))
					print ('Port: '+str(port))
		except :
			print ('Error connecting to: '+str(sys.argv[1]+'.'+str(host)) +':'+ str(port))
			pass
