#encoding: utf8
#script para la manipulacion de paquetes de la red con python
from scapy.all import IP, TCP, sr

rang = "192.168.0.1/24"

package = IP(dst=rang) / TCP()

response, unanswered = sr(package, timeout=2, verbose=False)    #verbose para ignorar toda la salida de texto de sr

for send, res in response:
    if res.flags == 2:
        print(send.dst)
