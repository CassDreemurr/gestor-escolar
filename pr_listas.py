"""lista = [1,2,2,3,1,4]
elementos = list(dict.fromkeys(lista))

print(elementos)"""

"""def minimo(lista):
    menor = lista[0]
    for n in lista:
        if n < menor:
            menor = n
        else:
            pass
    return menor

def maximo(lista):
    mayor = lista[0]
    for n in lista:
        if n > mayor:
            mayor = n
        else:
            pass
    return mayor

numeros = [19,3,4,0,1]
print(minimo(numeros))
print(maximo(numeros))"""

"""def descarte(lista):
    palabras_largas = []
    palabras_cortas = []
    for p in lista:
        if len(p) > 5:
            palabras_largas.append(p)
        else:
            palabras_cortas.append(p)
    return palabras_largas,palabras_cortas

palabras = ['chocolate','pasa','caramelo','nuez','fresa','uva','vainilla']
largas, cortas = descarte(palabras)
print(f"Las palabras largas son: {(largas)}.\nLas palabras cortas son: {cortas}")"""

"""lista = [1,2,3,4]
ultimo = lista.pop()
lista.insert(0,ultimo)


print(lista)"""

"""lista = [1,2,3,4]
lista = [n**2 for n in lista]

print(lista)"""