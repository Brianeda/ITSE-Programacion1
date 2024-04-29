numeros = [15, 15, 20, 20, 25, 30, 30, 50, 50, 100, 100, 1000, 1000]
aux = 0
bandera = False

for i in range(len(numeros)):
    for j in range(len(numeros)):
        if i != j:
            if numeros[i] == numeros[j] and bandera == False:
                bandera = True

    if bandera == False:
        aux = i
    bandera = False

print(numeros[aux])