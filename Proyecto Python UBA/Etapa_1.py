#en esta funcion ocultamos la palabra por incognitas donde cada letra a adivinar
#será reemplazado por el signo de incognita.
def palabra_incognita(palabra):#primer paso:recibo 'palabra' en mi función palabra_incognita
    incognita = ''#2°)Inicializo incognita para que sea una variable de tipo string.
    for i in range(len(palabra)):#recorro letra por letra que sería cada incognita
        incognita += '?'#acá agrega a cada letra a adivinar un signo de incognita.
    return incognita #3°) y me devuelve la incognita

#En esta función recibo la palabra y las letras ingresadas para agregarle una posición y almacenarla
#en la lista
def lista_posicion_de_letra(palabra, letra_ingresada):
    lista = [] #inicializo con una lista vacía. La lista me sirve para almacenar las letras que coinciden con la palabra
    i = 0#inicio el contador igual a 0. El contador cuenta las letras que hay dentro de la palabra 
    for letra in palabra:: #recorro letra(elemento) por letra(elemento) en la palabra y a su vez analizar las letras
        if letra == letra_ingresada: #si la letra que se encuentra en la palabra a adivinir es igual a la letra ingresada
            lista.append(i)#se agrega cada letra de la palabra en la lista
        i += 1#si pasa lo anterior el contador vuelve a recorrer.
    return lista#me devuelve la lista de las posiciones

#Si la letra se encuentra en la palabra a adivinar debe mostrar en las posiciones que se encuentra,
#lo que hago acá es reemplazar las incognitas por la letra ingresada si es que es acertada

def reemplazo_de_letra(palabra, incognita, letra_ingresada):
    palabra_lista = list(incognita)
    for i in lista_posicion_de_letra(palabra, letra_ingresada):
        palabra_lista[i] = letra_ingresada
    strA = ''
    return strA.join(palabra_lista)

#esta función se encarga de definir las condiciones del juego.
def lista_letras(lista_partida, letra_ingresada, incognita, registro):
    if letra_ingresada in registro:  
        print('Letra ya ingresada...', 'Aciertos:', lista_partida[4], 'Desaciertos:', lista_partida[5])
    else:
        if len(letra_ingresada) > 1 or not letra_ingresada.isalpha():
            print('Ingreso Inválido')
        elif letra_ingresada in lista_partida[0]:
            lista_partida[2].append(letra_ingresada)
            lista_partida[4] += 1
            registro.append(letra_ingresada)
            print('Muy bien!!!-->', incognita, 'Aciertos:', lista_partida[4], 'Desaciertos:', lista_partida[5])
        else:
            lista_partida[3].append(letra_ingresada)
            lista_partida[5] += 1
            registro.append(letra_ingresada)
            print('Lo siento!!!-->', incognita, 'Aciertos:', lista_partida[4], 'Desaciertos:', lista_partida[5])
    return

#esta función se encarga de almacenar las estadisiticas o datos de la partida.
def datos_partida(palabra, incognita):
    lista_partida = [palabra, incognita, [], [], 0, 0]
    return lista_partida

# 1) el main se encarga de recibir la palabra que luego la utilizaremos como incognita, a su vez se va a encargar de hacer un registro
#de las letras acertadas y desacertadas de la palabra. También se encarga de interrumpir el proceso en caso que se ingrese
#un valor distinto a lo definido, y, para finalizarlo.

# def main():
#     palabra = input('Ingrese una palabra: ')
#     incognita = palabra_incognita(palabra)
#     lista_partida = datos_partida(palabra, incognita)
#     registro = []
#     print('Palabra a adivinar:', incognita, 'Aciertos:', lista_partida[4], 'Desaciertos:', lista_partida[5])
#     letra_ingresada = input('Ingrese letra: ')
#     while incognita != palabra and letra_ingresada != '0' and letra_ingresada != 'FIN' and lista_partida[5] < 7:
#         incognita = reemplazo_de_letra(palabra, incognita, letra_ingresada)
#         lista_letras(lista_partida, letra_ingresada, incognita, registro)
#         if incognita != palabra:
#             letra_ingresada = input('Ingrese letra: ')
#     return
# main()
