
string = "Titulo"


#Imprimir centrado
print("{:*^30}".format(string))    #(caracter-posicion-espaciado)

#imprimir izquierda o derecha (  < ó  >  )


#porcentajes
puntos = 19
preguntas = 22

print("Correct answers: {:.2%}".format(puntos/preguntas))   #.2 es la precision y % el formato

print("Este es numero tiene una cifra decimal {:.1f}".format(1.000))    #otro ejemplo con float
