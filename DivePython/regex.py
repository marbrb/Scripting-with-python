import re

addr1 = "100 NORTH BROAD ROAD"
print(re.sub('ROAD$', 'RD', addr1))

addr2 = '100 BROAD ROAD APT. 3'
print(re.sub(r'\bROAD\b', 'RD', addr2)) # \b indica que debe existir en ese punto un límite de palabra

#roman numerals

pattern = r'^M?M?M?$'   # ? hace que un patron sea opcional, es decir pueden haber de 0-3 My el patron coincidirá

if re.search(pattern, 'MMM'): print("coincide")
if not re.search(pattern, 'MMMM'): print("no coincide")
if re.search(pattern, ''): print("coincide")
