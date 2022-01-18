import Etapa_2
import random

def longitud_palabra(diccionario):
    longitud_palabra = input('Elija la longitud de la palabra a adivinar: ')
    chequeo_longitud = 0
    while longitud_palabra != 0 and chequeo_longitud == 0:
        if longitud_palabra.isnumeric():
            longitud_palabra = int(longitud_palabra)
            for palabra in diccionario:
                if longitud_palabra == len(palabra):
                        chequeo_longitud += 1
            if longitud_palabra != 0 and chequeo_longitud == 0:
                print('No hay palabras con la longitud elegida')
                longitud_palabra = int(input('Elija la longitud de la palabra a adivinar: '))
        else:
            print('Ingrese un valor numérico.')
            longitud_palabra = input('Elija la longitud de la palabra a adivinar: ')
    return longitud_palabra

def palabras_candidatas(diccionario, largo_palabra):
    lista_palabras = []
    if largo_palabra == 0:
        for palabra in diccionario:
            if len(palabra) >= 5:
                lista_palabras.append(palabra)
    else:
        for palabra in diccionario:
            if largo_palabra == len(palabra):
                lista_palabras.append(palabra)
    return lista_palabras

def seleccion_palabra_aleatoria(diccionario, largo_palabra, lista_palabras):
    palabra = random.choice(lista_palabras)
    return palabra

# def main():
#     diccionario = Etapa_2.procesar_texto()
#     largo_palabra = longitud_palabra(diccionario)
#     lista_palabras = palabras_candidatas(diccionario, largo_palabra)
#     palabra = seleccion_palabra_aleatoria(diccionario, largo_palabra, lista_palabras)
#     print(palabra)
#     
# main()