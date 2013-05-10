# Set de problemas #2
# Problema 2.
# Lenguaje y Tecnicas de Programacion
# Profesor: Igor Caracci
# Profesor(Ayudante): Andres Caro
# Universidad de Santiago de Chile
# 07 de mayo del 2013
#
# Descripcion:
# Este programa tiene una función es_palindroma(str) que retorne True
# si el string str ingresado es palíndromo o False en caso contrario. 
# La función utiliza listas para la verificación.
 

def es_palindroma(str): #Funcion que ve si el string es palindrome
    return (str==str[::-1])

def main():
    str = input("Ingrese un string \n") #Solicito el string para proceso
    if (es_palindroma(str)):
        print("El string ", str," es palindrome") #Imprimo
    else:
        print("El string ", str," no es palindrome") #Imprimo
    
    return 0;

if __name__ == "__main__": #Si ejecuta como programa invoca a main
    main()
  

