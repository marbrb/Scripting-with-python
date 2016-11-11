#!/usr/bin/env python3
import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):
    path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
    connection = http.client.HTTPConnection('10.20.4.15', 3128)
    connection.set_tunnel('maps.google.com')
    connection.request('GET', path)
    raw_reply = connection.getresponse().read() #HTTPResponse on bytes
    reply = json.loads(raw_reply.decode('utf-8'))   #decode bytes and parse to json
    return(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
    print(geocode('207 N, Defiance St, Archbold, OH'))
