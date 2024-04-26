n1 = 0
n2 = 0

print("Ingrese un numero A: ")
n1 = int(input())
print("Ingrese un numero B: ")
n2 = int(input())

if n1 == n2:
    print("El numero A y B son iguales")
elif n1>=n2:
    print("El numero A es mayor que el numero B")
else:
    print("El numero B es mayor que el numero A")