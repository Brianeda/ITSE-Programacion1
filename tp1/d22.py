posi = 0
nega = 0
aux1 = 0

for i in range(6):
    num = int(input("Ingrese el " + str(i+1) + "° numero entero: "))
    if num > 0:
        posi = posi + num
        aux1 += 1
    else:
        nega = nega + num

posi /= aux1

print("El promedio de los positivos es: " + str(posi))
print("La sumatoria de los negativos es: " + str(nega))
