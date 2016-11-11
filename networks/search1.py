#!/usr/bin/env python3
from pygeocoder import Geocoder

if __name__ == "__main__":
    address = '201 N. Defiance St, Archbold, OH'
    coder = Geocoder()
    coder.set_proxy('10.20.4.15:3128')
    print(coder.geocode(address)[0].coordinates)
