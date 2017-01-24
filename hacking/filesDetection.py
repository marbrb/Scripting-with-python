#encoding: utf8
import requests
import argparse
import re #librería para manejo de regex

#robots.txt le dice a los bots de los motores de busqueda a que directorios no pueden acceder
#phpinfo.php  contiene informacion del sistema, versiones de sistema, mysql, php... rutas del servidor

def robotsDetection(url):
    fileName = "/robots.txt"
    try:
        connection = requests.get(url= url+fileName) #conectarse a la url por metodo get
    except:
        print("No se pudo conectar a la url")
        return False

    if connection.status_code == 200:   #codigo 200 quiere decir conexion satisfactoria
        print("Archivo {} encontrado!".format(fileName))
        lines = connection.text.split("\n")
        return lines

    else:
        print("No se encontro el archivo {}".format(fileName))

def phpinfoDetection(url):
    fileName = "/phpinfo.php"
    try:
        connection = requests.get(url= url+fileName) #conectarse a la url por metodo get
    except:
        print("No se pudo conectar a la url")
        return False
    if connection.status_code == 200:   #codigo 200 quiere decir conexion satisfactoria
        print("Archivo {} encontrado!".format(fileName))
        regexPhp = '(<tr class="h"><td>\n|alt="PHP Logo" /></a>)<h1 class="p">(.*?)</h1>'
        regexSystem = 'System </td><td class="v">(.*?)</td></tr>'
        responseBody = connection.text
        findPhp = re.search(regexPhp, responseBody)
        findSystem = re.search(regexSystem, responseBody)
        systemInformation = list()

        if findPhp:
            systemInformation.append(findPhp.group(2))    #El 2 hace referencia a el segundo valor capturado en l regexPhp
        else:
            print("No se pudo detectar la versión de PHP")

        if findSystem:
            systemInformation.append(findSystem.group(1))
        else:
            print("No se pudo detectar la versión del sistema")

        return systemInformation
    else:
        print("No se pudo encontrar el archivo {}".format(fileName))
        return False



def main():
    parser  = argparse.ArgumentParser(description= "Script para detectar archivos sensibles")
    parser.add_argument(
        "-u", "--url", dest="website_url", help="Especifica la URL completa", required=True
        )
    arguments = parser.parse_args()

    if arguments.website_url:
        robotsResponse = robotsDetection(arguments.website_url)
        if robotsResponse:  #Si la lista tiene contenido retorna True
            for line in robotsResponse:
                if line.startswith("Disallow:"):
                    print(line)
        phpRespose = phpinfoDetection(arguments.website_url)
        if phpRespose:
            print("Version de PHP : {}".format(phpRespose[0]))
            print("Version del sistema : {}".format(phpRespose[1]))

    else:
        print("No hay url a la cual conectarse")

if __name__ == '__main__':
    main()
