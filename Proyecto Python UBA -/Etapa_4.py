'''En esta etapa decía que debemos integrar las funcionalidades resueltas en cada una de las
etapas anteriores'''
import Etapa_1
import Etapa_2
import Etapa_3
import random
import Etapa_5

def main():
    #Se deberá comenzar con la generación del diccionario de palabras.
    diccionario = Etapa_2.procesar_texto() #llamo a la función procesar texto de la etapa 2 y a este proceso lo llamamos diccionario
    #Luego se debe solicitar al jugador, que ingrese la longitud de la palabra que desea adivinar, validando dicho ingreso
    largo_palabra = Etapa_3.longitud_palabra(diccionario) #llamo a la función longitud palabra
    #En caso de no ingresar ningún valor, todas las palabras serán candidatas; sino sólo aquellas que cumplan con dicha longitud.
    lista_palabras = Etapa_3.palabras_candidatas(diccionario, largo_palabra) #llamo a la función palabras candidatas
    #El programa elegirá al azar una palabra a adivinar por el jugador.
    palabra = Etapa_3.seleccion_palabra_aleatoria(diccionario, largo_palabra, lista_palabras)
    #Elegida la palabra, mostrará tantos signos de pregunta como letras compongan la palabra elegida
    incognita = Etapa_1.palabra_incognita(palabra)
    #a continuación le pedirá al jugador que ingrese una letra,implementando así, lo realizado en la etapa 1
    lista_partida = Etapa_1.datos_partida(palabra, incognita)
    registro = [] #inicializo el registro con una lista vacía, que es donde almaceno las letras ingresadas
    puntaje = 0 #inicializo el contador de puntaje
    continuar = True #cuando mi variable continuar sea verdadera continúa con la partida
    print('Palabra a adivinar:', incognita, 'Aciertos:', lista_partida[4], 'Desaciertos:', lista_partida[5]) #esto me ir imprimiendo palabra a adividar, aciertos...
    print('Puntos:', puntaje) #y tambien imprime el puntaje que iniciaba en 0
    letra_ingresada = input('Ingrese letra: ') #despues me va pedir el ingreso de las letras
    while continuar: #mientras yo continúe la partida tengo las siguientes condiciones
        while incognita != palabra and letra_ingresada != '0' and letra_ingresada != 'FIN' and lista_partida[5] < 7 and continuar: #mientras no se finalice el ciclo while el codigo me va ejecutar estas condiciones y que yo continue con la partida... // que mientras las condiciones sean distintas a lo mencionado anteriormente, o sea que la incognita sea distinta a la palabra, y si ingreso '0' o FIN y que se supere los 7 desaciertos se finalice el ciclo y deseo continuar
            puntaje = Etapa_5.puntaje_partida(palabra, lista_partida, letra_ingresada, puntaje) #defino puntaje #llamo a la función puntaje_partida de la Etapa_5 con sus parametros que me va ir contando los puntos
            incognita = Etapa_1.reemplazo_de_letra(palabra, incognita, letra_ingresada) #defino incognita #llamo a la función reemplazo de letra de la Etapa_1 para que reemplace las letras por incognitas
            Etapa_1.lista_letras(lista_partida, letra_ingresada, incognita, registro) #llamo a lista_letras con sus parametros
            print('Puntos:', puntaje) #y me imprime los puntos del puntaje
            if incognita != palabra: #y si la letra ingresada es distinta de la incognita 
                letra_ingresada = input('Ingrese letra: ') #me vuelve a pedir el ingreso de una letra
        if lista_partida[5] >= 7: #y ponemos esta condición de que si la cantidad de desaciertos(que está en la lista_partida posición 5) es mayor o igual a 7
            Etapa_1.lista_letras(lista_partida, letra_ingresada, incognita, registro) #llamo a lista_letras con sus parametros 
            puntaje = puntaje - 2 # y al puntaje se le va restar 2 cada vez que tenga un desacierto 
            print('Puntos:', puntaje) #y me imprime el puntaje actual
        continuar = Etapa_5.continuar_partida() #llamo a la función continuar que me va preguntar si deseo seguir continuando
        if continuar:
            #ya no llamo al diccionario de la etapa 2, sigo con el mismo diccionario 
            largo_palabra = Etapa_3.longitud_palabra(diccionario)
            lista_palabras = Etapa_3.palabras_candidatas(diccionario, largo_palabra)
            palabra = Etapa_3.seleccion_palabra_aleatoria(diccionario, largo_palabra, lista_palabras)
            incognita = Etapa_1.palabra_incognita(palabra)
            lista_partida = Etapa_1.datos_partida(palabra, incognita)
            registro = []
            print('Palabra a adivinar:', incognita, 'Aciertos:', lista_partida[4], 'Desaciertos:', lista_partida[5])
            print('Puntos:', puntaje)
            letra_ingresada = input('Ingrese letra: ')
    print('Puntaje final:', puntaje)
main()
