#!/usr/bin/env python3
import requests

def geocode(address):
    parameters = {'address':address, 'sensor':'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    return (answer['results'][0]['geometry']['location'])

if __name__ == "__main__":
    print(geocode('207 N. Defiance St, Archbold, OH'))
