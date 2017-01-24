#encoding : utf8
import requests
import argparse
from bs4 import BeautifulSoup   #html a un formato DI-VI-NO
class WebInformation():
    def __init__(self, url):
        self.url = url

    #se encarga de extraer informacion de los sitios que estan alojados en el mismo servidor que la url que pasamos
    def reverseIP(self):
        #acomodar la url como la necesitamos (www.url.com)
        if self.url.startswith("http://"):
            url = self.url.replace("http://","") #remplazar por vacio :v
        else:
            url = self.url

        #se envia por post ya que la pagina usa un formulario para pedir la url a escanear
        #data son los datos POST que es la url
        #remoteHost es como se envía el parametro (la url que se especifica en connection)
        data = {"remoteHost" : url}
        connection = requests.post(
            #parametros necesarios para la conexion
            url="http://www.ipfingerprints.com/scripts/getReverseIP.php", data=data
        )

        #connection.text es el html que retorna la conexion
        #BeautifulSoup lo parsea menos horrible
        #html.parser para salida mas limpia
        beautifulOut = BeautifulSoup(connection.text, "html.parser")

        #aqui guardaremos todos los links que encontremos en la etiqueta
        response = list()

        #find_all busca todas las equitas y 'a' es el parametro para filtrar solo ese tipo de etiqueta
        for link in beautifulOut.find_all("a"):
            #href es el nombre del dominio (que es lo unico que nos interesa de toda la etiqueta)
            currentLink = link.get("href")
            response.append(currentLink[11:-2])

        return response

    #busca que tecnología está usando el servidor
    def searchServer(self):
        #acomodar la url como la necesitamos "http://url.com"
        url = self.url
        if not self.url.startswith("http://"):
            if self.url.startswith("www"):
                url = "http://"+self.url
            elif not self.url.startswith("www"):
                url = "http://www."+self.url
            else:
                return "BAD URL :-("

        #verify es para que no de problemas si la url no tiene habilitado SSL
        connection = requests.get(url=url, verify=False)
        #connection.headers.get retorna un diccionario y .get() busca la clave 'server'
        headers = connection.headers.get("server")
        return headers

def main():
    parser = argparse.ArgumentParser(description="Tool para escanear")
    parser.add_argument("-u", "--url", dest="target_url", help="URL del sitio a escanear", required=True)

    #si pasa el argumento, guarda True en server
    parser.add_argument("-s", "--server", help="Extraer tecnología del servidor", action="store_true")
    parser.add_argument("-r", "--reverse", help="Extraer sitios alojados en el servidor", action="store_true")

    arguments = parser.parse_args()

    if arguments.server:
        extractor = WebInformation(arguments.target_url)
        print(extractor.searchServer())

    if arguments.reverse:
        extractor = WebInformation(arguments.target_url)
        sites = extractor.reverseIP()
        for site in sites:
            print(site)

if __name__ == '__main__':
    main()
