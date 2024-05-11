lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if not lista:
    raise ValueError("La lista esá vacía")
elif len(lista) % 2 != 0:
    aux1 = int(len(lista) / 2)
    print("La mediana de la lista es: " + str(lista[aux1]))
elif len(lista) % 2 == 0:
    aux1 = int((len(lista) / 2) - 1)
    aux2 = int(len(lista) / 2)
    print("Las 2 medianas de la lista son: " + str(lista[aux1]) + " y " + str(lista[aux2]))