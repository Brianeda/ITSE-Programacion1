num = int(input("Ingrese la cantidad de iteraciones: "))
total = 0

for i in range(0, num, 1):
    total = total + int(input("Ingrese un numero para sumar al total: "))

print("El total de la suma es: " + str(total))