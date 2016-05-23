#encoding: utf8
import subprocess #sustituye a os.sistem que permitia ejecutar comandos en el sistema
import os

dontOut = open(os.devnull, "w") #equivalente a redirigir el flujo de salida a /dev/null

def ping(ip):

    #pasamos el comando que deseamos ejecutar en forma de lista, "-c" es la cantidad
    #stderr es para manejo de errores
    response = subprocess.call(
        ["ping", "-c", "2", ip], stdout=dontOut, stderr=subprocess.STDOUT
    )

    if response == 0:   #Esto significa que la maquita esta respondiendo :D
        print("La máquina está viva wuey!")

    else:   #si responde 1 es porque la maquina no responde y otro número es por un error
        print("La máquina está muelta :c")

print("Digite la IP ó 'hecho' si no quiere conectarse a más IPs")

while True:
    ip = input("> ")

    if ip == "hecho":
        break
    ping(ip)
