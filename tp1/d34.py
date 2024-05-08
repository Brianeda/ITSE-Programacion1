lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(lista) % 2 != 0:
    aux = int(len(lista) / 2)
    print("La mediana de la lista es: " + str(lista[aux]))