import nmap

victimHost = "192.168.0.13"
arguments = "-sV -p80"  #sV es apra la version del puerto

scanner = nmap.PortScanner()
scanner.scan(hosts=victimHost, arguments=arguments)
result = scanner[victimHost]["tcp"][80]     #filtrar los resultados del escaneo
for key in result.keys():
    #result es un dict
    data = key + " : " + result[key]
    print(data)
