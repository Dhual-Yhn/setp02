# Set de problemas #2
# Problema 3.
# Lenguaje y Tecnicas de Programacion
# Profesor: Igor Caracci
# Profesor(Ayudante): Andres Caro
# Universidad de Santiago de Chile
# 07 de mayo del 2013
#
# Descripcion:
# para este problema debe tomar el cuento y utilizar un diccionario para
# almacenar la cantidad de veces que cada palabra aparece en el cuento.
# Para esto considere que "Funes", "FUNES" y "funes" cuentan como la misma
# palabra. La salida del programa debe ser cada palabra con su respectiva
# cuenta, ordenadas de mayor a menor.

import re   #Libreria para expresiones regulares

dic_cuento={} #Declaro diccionario
archivo = open('funes.txt','r',encoding='utf-8') #Abro archivo (encoding='utf-8') sirve para considerar los acentos de las palabras
conten=archivo.read().lower() #Paso todo a minusculas
archivo.close() #Cierro archivo
palabras=re.split('[^a-záéíóúñü]*',conten) #Busco palabras

for pal in palabras:            #Recorro lista palabras
    if (pal in dic_cuento):     #Chequeo si las conte
        dic_cuento[pal]=dic_cuento[pal]+1   #Si ya figura, incremento
    else:
        dic_cuento[pal]=1   #Si no figura, la agrego

for w in sorted(dic_cuento, key=dic_cuento.get, reverse=True): #Ordena diccionario de mayor a menor y lo recorro
    print(w, dic_cuento[w])  #Imprimo lo solicitado
