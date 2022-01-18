def solicitar_texto(mensaje):
    texto = input(mensaje)
    return texto

def procesar_texto():
    parrafo = solicitar_texto('Ingrese el texto: ')
    parrafo = parrafo.lower()
    parrafo = parrafo.replace(',','')
    parrafo = parrafo.replace('.','')
    parrafo = parrafo.replace(':','')
    parrafo = parrafo.replace(';','')
    diccionario = {}
    lista = parrafo.split(' ')
    total_palabras = 0
    for palabra in lista:
        if len(palabra) >= 5 and palabra.isalpha() and palabra not in diccionario:
            diccionario[palabra] = 1
            total_palabras += 1
        elif len(palabra) >= 5 and palabra.isalpha():
            diccionario[palabra] += 1
#     diccionario_ordenado = sorted(diccionario.items())
#     for palabra in diccionario_ordenado:
#         print(palabra)
    print('El total de palabras es:', total_palabras)
    return diccionario
    
# def main():
#   p = procesar_texto()      
# main()