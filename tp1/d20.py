num = int(input("Ingrese un numero entero positivo: "))
total = 1

for i in range(1, num, 1):
    total = total * (i+1)

print("Su factorial es: " + str(total))