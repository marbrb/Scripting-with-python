#encoding: utf8
#description: script para automatizar la detección de vulnerabilidades de ti SQL injection
#funcionamiento: conectarse a un sitio, extraer links del sitio y comparalos con una regex
#para ver si son de la típica forma de un sitio vulnerable "algo.php?otroAlgo=int"

import argparse
import requests
import re
from bs4 import BeautifulSoup
from multiprocessing import Pool    #librería para multiprocesos
import time

parser = argparse.ArgumentParser(description="script para detectar la vulnerabilidad de tipo SQL injection")
parser.add_argument("-u", "--url", dest="target_url", help="URL del sitio a escanear", required=True)
arguments = parser.parse_args()

def verifyVulnerability(url):
    connection = browser.get(url)
    if "You have an error in your SQL syntax" in connection.text:
        print("{} es vulnerable".format(url))
    else:
        print("{}  NO es vulnerable".format(url))



if arguments.target_url:
    browser = requests.Session()    #simular un navergador para mantener la sesion por medio de una cookie, y no a con hilos como en los otros programas
    connection = browser.get(arguments.target_url)  #metodo get
    response = connection.text  #retorna un HTML
    soup = BeautifulSoup(response, "html.parser")  #renderiza el HTML
    posibleVulnerablesLinks = list()
    for x in soup.find_all("a"):    #etiqueta "a" para buscar todos los links
        link = x.get("href")

        # "<=" hace que se ignore lo que hay entre "?" y el ultimo "="
        # "\w+" significa que se va a recibir un parametro sin importar si
        # es número o letra (el "+" quiere decir que no import el largo)
        if re.search("(?<==)\w+", link):
            posibleVulnerablesLinks.append(link)    #si el link cumple con la regex, es vulnerable
        else:
            pass

if posibleVulnerablesLinks:
    try:
        pool = Pool(processes=1)
        h = pool.map(verifyVulnerability,
        (arguments.target_url + url + "'" for url in posibleVulnerablesLinks)) # %27 es como el navergador reconoce una comilla simple
        time.sleep(1)
        #pagina.com + / parte vulnerable + la comilla
    except:
        pass
