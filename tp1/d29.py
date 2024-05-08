lista = []
bandera = True
aux = 0

alfa = input("Introduce un dato alfanumérico: ")
carac = input("Introduce un caracter: ")

for i in range(len(alfa)):
    for j in range(len(alfa)):
        if carac != alfa[j] and bandera == True and j >= i:
            aux += 1
        elif j < i:
            bandera = True
        else:
            bandera = False

    lista.append(aux)
    aux = 0
    bandera = True

bandera = True
for i in range(1, len(lista)):
    if lista[-i] != 0 and bandera == True:
        lista[-i] = "No hay incidencias del caracter introducido hacia adelante"
    elif lista[-i] == 0:
        bandera = False

for i in range(len(lista)):
    print("Desde el " + str(i+1) + "° caracter (" + str(alfa[i]) + ") hasta encontrarse con incidencia de " + str(carac) + " hay una cantidad de distancia de: " + str(lista[i]))