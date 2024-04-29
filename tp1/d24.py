n1 = int(input("Ingrese el 1° año: "))
n2 = int(input("Ingrese el 2° año: "))

if n1 < n2:
    rango = range(n1, n2 + 1)
else:
    rango = range(n2, n1 + 1)

print("Lista de años bisiestos y múltiplos de 10 que hay entre los años ingresados: ")

for año in rango:
    if ((año % 4 == 0 and año % 100 != 0) or año % 400 == 0) and año % 10 == 0:
        print(año)