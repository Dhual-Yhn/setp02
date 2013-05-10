# Set de problemas #2
# Problema 4.
# Lenguaje y Tecnicas de Programacion
# Profesor: Igor Caracci
# Profesor(Ayudante): Andres Caro
# Universidad de Santiago de Chile
# 07 de mayo del 2013
#
# Descripcion:
#
# Este script, contiene una función combinatoria2(set, k) que determina todas
# las k-tuplas que se pueden formar con el conjunto set.
# La función debe retornar una lista con las tuplas.

#Determina todas las k-tuplas que se pueden formar con el conjunto set
def combinatoria2(set, k):

#Podemos crear rangos que vayan desde un numero x al infinito, lo cual
    import itertools

    lista_vacia = []

    for combination in itertools.combinations(set, k):
        #Agregando al final de una lista la combinacion
        lista_vacia.append(combination)
     
    #Retorno las combinaciones posibles
    return lista_vacia

set = set()

while True:
    valor = input("Cantidad de elementos a ingresar al conjunto : ")
    if ( not valor.isnumeric() ):
         print("Error, ",valor," no es un numero ")
    elif ( int(valor) < 1 ):
         print("Error, numero ",valor," menor a 1")
    else:
    #Ciclo que llena con elementos ingresados por usuario
         for x in range(0, int(valor)):
             ingreso = input("Ingrese elemento: ")
             set.add(ingreso) #Añado elemento al set
         break

total = int(valor)
while True:
    print("Ingrese un 'k' > que 0 y menor o igual a ", total)    
    valor = input()
    
    if ( not valor.isnumeric() ):
        print("Error, ",valor," no es un numero ")
    elif ( int(valor) > total or int(valor) < 1 ):
        print("Error, numero ",valor," no valido (>",total," o <1")
    else:
        break

k = int(valor)
lista_combi = combinatoria2(set, k)     
for ingreso in lista_combi:
    print(ingreso, "\n")
