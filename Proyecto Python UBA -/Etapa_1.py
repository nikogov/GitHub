def palabra_incognita(palabra):
    incognita = ''
    for i in range(len(palabra)):
        incognita += '?'
    return incognita

def lista_posicion_de_letra(palabra, letra_ingresada):
    lista = []
    i = 0
    for letra in palabra:
        if letra == letra_ingresada:
            lista.append(i)
        i += 1
    return lista

def reemplazo_de_letra(palabra, incognita, letra_ingresada):
    palabra_lista = list(incognita)
    for i in lista_posicion_de_letra(palabra, letra_ingresada):
        palabra_lista[i] = letra_ingresada
    strA = ''
    return strA.join(palabra_lista)

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

def datos_partida(palabra, incognita):
    lista_partida = [palabra, incognita, [], [], 0, 0]
    return lista_partida


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