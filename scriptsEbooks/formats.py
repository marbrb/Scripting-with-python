#!/usr/bin/python3
#coding: utf8
string = "Titulo"


#Imprimir centrado
print("{:*^30}".format(string))    #(caracter-posicion-espaciado)

#imprimir izquierda o derecha (  < ó  >  )


#porcentajes
puntos = 19.5         #alguno tiene que ser float
preguntas = 22.0    #alguno tiene que ser float

print("Correct answers: {:.2%}".format(puntos/preguntas))   #.2 es la precision y % el formato

print("Este es numero tiene una cifra decimal {:.1f}".format(1.30400))    #otro ejemplo con float

#------BASES-------

print('int: {0:d}  oct: {0:o}  hex: {0:x}  bin: {0:b}.'.format(42))


#------BYTES-------

by = b'd'
string = 'a b c d e'

print(string.count(by.decode('ascii')))    #hay que decodificar los bytes para poder buscar las ocurrencias en el string

