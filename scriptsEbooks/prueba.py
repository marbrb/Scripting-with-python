a = [1,2,3]
b = [1,2,3]

#enumerate() retorna un iterable de (indice, lista[indice])
for indice, item in enumerate(a):
    print("indice: {}  -  item: {}". format(indice, iteam))

#zip() retorna tuplas de el i-ésimo item de cada iterable
for x, y in zip(a,b):
    print("paired items: ({},{})".format(x,y))

#example of List Comprehensions
lista_impares_de_a = [x for x in a if x%2!=0]

import os, glob

print(os.getcwd())  #print out current path

os.chdir('/home/miguel/Imágenes')   #change dir

print(glob.glob('*.png'))   #print out list of images in the current dir

#example of sets

a = set()   #empty set

a.add(1)
a.update({1,2,3})   #take set(s) as argument

