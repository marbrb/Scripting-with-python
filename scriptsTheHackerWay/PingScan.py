#!/usr/bin/env python
#Descripcion: Script para detectar maquinas activas en un segmento de red
#ping utiliza el protocolo ICMP , que es un protocolo simple para el intercambio de mensajes entre maquinas

#funcionamiento: envia un mensaje de tipo ECHO_REQUEST  y espera una respuesta del tipo ECHO_REPLY

from subprocess import Popen, PIPE

for ip in range(1,40):
	ipAddress = '192.168.1.'+str(ip)
	print "Scanning %s " %(ipAddress)
	subprocess = Popen(['/bin/ping', '-c 1 ', ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE)#flujos de entrada, salida y error son del tipo PIPE
	stdout, stderr= subprocess.communicate(input=None)	# esto ejecuta lo qe hay en subprocess(el ping) y guarda el flujo de salida y de error
	if "bytes from " in stdout:
		print "The Ip Address %s has responded with a ECHO_REPLY!" %(stdout.split()[1])	#divide por espacios toda la salida de ping y la posicion 1 es el num de IP

	#	with open("ips.txt", "a") as myfile:	#abre el archivo y lo guarda en myfile y luego lo cierra
	#		myfile.write(stdout.split()[1]+'\n')
#comentado para no crear archivos en la ejecucion
