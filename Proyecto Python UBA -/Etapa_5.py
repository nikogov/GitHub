'''Etapa 5 - Puntaje
Hasta ahora nuestro jugador, simplemente gana o pierde.
En esta etapa vamos a permitir que obtenga puntaje y que el mismo se acumule de
partida en partida.
Si la letra elegida por el jugador se encuentra en la palabra, obtendrá un punto por
haber acertado, de lo contrario, se le restarán 2 puntos. El puntaje final obtenido
podrá ser negativo.
Al finalizar una partida, se le ofrecerá si desea jugar otra; así hasta que responda
que no. El puntaje obtenido en la última partida, se tomará como inicio de la actual.
Al inicio de la ejecución del 1er. juego, el puntaje se encuentra en cero.'''
import random 

#esta función va permitir que obtenga puntaje y que se acumule de partida en partida
def puntaje_partida(palabra, lista_partida, letra_ingresada, puntaje): #defino puntaje partida que recibe esos parámetros
    if letra_ingresada in palabra and letra_ingresada not in lista_partida[2] and letra_ingresada.isalpha() and len(letra_ingresada) == 1: #creamos una condición de que si la letra ingresada está en la palabra y si la le letra ingresada no está en la lista de aciertos repetida y si la letra ingresada es alfabetica y la longitud de la letra es igual a 1 
        puntaje += 1 #puntaje = puntaje + 1 'al contador puntaje se le suma 1', este contador se inicializo en la etapa_4
    elif letra_ingresada not in palabra and letra_ingresada not in lista_partida[3] and letra_ingresada.isalpha() and len(letra_ingresada) == 1: #y si la letra ingresada no está en la palabra y la letra ingresada no está en la lista de desaciertos repetida y la letra es alfabetica y de longitud igual a 1
        puntaje += -2 #al puntaje le resto 2 puntos
    return puntaje #me devuelve el puntaje

#esta función ofrece al usuario si quiere continuar con la partida
def continuar_partida():
    seguir_jugando = input('¿Desea continuar jugando?: ') #a mi variable seguir_jugando le asigno un input que me va preguntar si quiero seguir jugando
    if seguir_jugando == 'si': #cuando ingreso 'si' 
        continuar = True #la condición continuar se hace verdadera con este boolean y sigue la partida
    elif seguir_jugando == 'no': #si ingreso 'no'
        continuar = False #la condición continuar se hace falsa y no sigue la partida
    else: #sino
        print('Debe ingresar "si" o "no"') #si no ingreso 'si' o 'no', imprime que debo cumplir con la condición de ingresar si o no
        continuar = continuar_partida() #y vuelve a llamar a llamar a la función continuar partida 
    return continuar #me devuelve continuar