print("Ingrese el primer nombre: ")
n1 = input()
print("Ingrese el segundo nombre: ")
n2 = input()

aux1 = n1[0]
aux2 = ""


x = 0
for x in range(len(n1)):
    if x == len(n1)-1:
        aux2 = n1[x]

if aux1 == n2[0] or aux2 == n2[len(n2)-1]:
    print("Coincidencia")
else:
    print("No hay coincidencia")

#print(aux1)
#print(aux2)