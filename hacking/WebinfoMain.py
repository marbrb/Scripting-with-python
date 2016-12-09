#encoding: utf8
import argparse
from webinfo import WebInformation

#funcion que se encarga de leer los parametros recibidos
parser = argparse.ArgumentParser(description="Tool para escanear")
#dest es el destino donde se va a almacenar el argumento que pase el usuario (target_url)
parser.add_argument("-u", "--url", dest="target_url", help="URL del sitio a escanear", required=True)

#si pasa el argumento, guarda True en server
parser.add_argument("-s", "--server", help="Extraer tecnología del servidor", action="store_true")
parser.add_argument("-r", "--reverse", help="Extraer sitios alojados en el servidor", action="store_true")

# "parsea" los argumentos recibidos
arguments = parser.parse_args()

if arguments.server:
    extractor = WebInformation(arguments.target_url)
    print(extractor.searchServer())

if arguments.reverse:
    extractor = WebInformation(arguments.target_url)
    sites = extractor.reverseIP()
    for site in sites:
        print(site)
