def cuadrado_perfecto(numero):
    lista = []
    for i in range(1, numero, 1):
        aux = i * i
        if aux % 2 != 0:
            lista.append(aux)
    return lista

print(cuadrado_perfecto(25))