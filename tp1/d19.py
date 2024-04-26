total = 0

for i in range(0, 101, 1):
    if i%3 == 0:
        total = total + i

print("La suma total de los numeros multiplos de 3 que están entre 0 y 100 es: " + str(total))