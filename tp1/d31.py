lista = []
total = 0

numero = input("Introduzca un número: ")

for i in numero:
    lista.append(i)

for i in range(len(lista)):
    total += int(lista[i])

print("La suma de los dígitos de " + str(numero) + " es: " + str(total))