# Set de problemas #2
# Problema 5.
# Lenguaje y Tecnicas de Programacion
# Profesor: Igor Caracci
# Profesor(Ayudante): Andres Caro
# Universidad de Santiago de Chile
# 07 de mayo del 2013
#
# Descripcion:
#
# Programa del juego clasico "cachipun"

def ganador_cachipun(lista):

        # Verifico numero de jugadores
        if ( len(lista) != 2 ):
            raise Exception ("Numero incorrecto de jugadores")

        # Verifico jugadas realizadas
        if ( lista[0][1] != 'R' and lista[0][1] != 'P' and lista[0][1] != 'T' ):
            raise Exception ("Jugada no valida")

        # Veo los posibles resultados
        if ( lista[0][1] == lista[1][1] ):
            print( "Ganador : ",lista[0][0]," Jugada: ",lista[0][1] )
        elif ( lista[0][1] == 'P' and lista[1][1] == 'R' ):
            print( "Ganador : ",lista[0][0]," Jugada: ",lista[0][1] )
        elif (lista[0][1] == 'P'):
            print( "Ganador : ",lista[1][0]," Jugada: ",lista[1][1] )
       	elif ( lista[0][1] == 'R' and lista[1][1] == 'P' ):
            print( "Ganador : ",lista[1][0]," Jugada: ",lista[1][1] )
        elif (lista[0][1] == 'R'):
            print( "Ganador : ",lista[0][0]," Jugada: ",lista[0][1] )
       	elif ( lista[0][1] == 'T' and lista[1][1] == 'P' ):
            print( "Ganador : ",lista[0][0]," Jugada: ",lista[0][1] )
        else:
            print( "Ganador : ",lista[1][0]," Jugada: ",lista[1][1] )
        return

lista = []
while True:
     nombre = input('Ingrese nombre del jugador, 0 para terminar : ');
     if ( nombre == '0' ):
        break
     jugada = input('Ingrese jugada (R/T/P) :').upper();
     juego = []
     juego.append (nombre)
     juego.append (jugada)
     lista.append (juego)

ganador_cachipun(lista)
