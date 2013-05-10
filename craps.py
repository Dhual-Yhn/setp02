# Set de problemas #2
# Problema 6.
# Lenguaje y Tecnicas de Programacion
# Profesor: Igor Caracci
# Profesor(Ayudante): Andres Caro
# Universidad de Santiago de Chile
# 07 de mayo del 2013
#
# Descripcion:
#
# Programa que simula el juego Craps

# Libreria que permite random.randint() osea, numeros enteros aleatorios
import random

# Creo 13 secuencia en dado
dado = []
for i in range (13):
    dado.append([])

# Creo 36 2-tuplas en dado con indice suma
for i in range (1,7):
    for j in range (1,7):
        dado[i+j].append( (i,j) )

# Creo el conjunto de secuencias que pierde
pierdes=set(dado[2]).union(dado[3],dado[12])

# Creo el conjunto de secuencias que gana
ganas=set(dado[7]).union(dado[11])

# Bandera para primer tiro
primero = True

# Ciclo del juego
while True:

    # Obtengo tiros aleatorios en ambos dados
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)

    # Creo tiro con el resultado de los dados
    tiro = (dado1,dado2)

    if ( primero ):
       
        # Verifico resultado del primer tiro
        if ( tiro in pierdes ):
            print(tiro,' Pierdes')
            break
        elif ( tiro in ganas ):
            print(tiro,' Ganas')
            break
        else:
            print(tiro,' Continuas')
            
            # Bandera para tiros siguientes
            primero = False

            # Defino valor del punto
            punto = dado1+dado2
    else:

        # Calculo el valor del tiro
        valor = dado1+dado2

        # Verifico el resultado en los sgtes tiros
        if ( valor == punto ):
            print(tiro,' Ganas')
            break
        elif ( valor == 7 ):
            print(tiro,' Pierdes')
            break
        else:
            print(tiro,' Continuas')
