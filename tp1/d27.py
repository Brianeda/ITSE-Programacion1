nombre = ""
lista1 = []
lista2 = []
lista1nr = []
lista2nr = []
lista1nr2 = []
listacomun = []

print("Ingrese la lista de nombres de los alumnos de 1°:  ")
while nombre != "S":
    nombre = input()
    lista1.append(nombre)

nombre = ""

print("Ingrese la lista de nombres de los alumnos de 2°:  ")
while nombre != "S":
    nombre = input()
    lista2.append(nombre)

for elemento in lista1:
    if (elemento not in lista1nr) and elemento != "S":
        lista1nr.append(elemento)

for elemento in lista2:
    if (elemento not in lista2nr) and elemento != "S":
        lista2nr.append(elemento)

print("Lista de los alumnos de 1° sin nombres repetidos: ")
for i in range(len(lista1nr)):
    print(lista1nr[i])

print("Lista de los alumnos de 2° sin nombres repetidos: ")
for i in range(len(lista2nr)):
    print(lista2nr[i])

print("Lista de los alumnos de 1° y 2° con nombres repetidos: ")
if len(lista1nr) > len(lista2nr):
    for elemento in lista1nr:
        if elemento in lista2nr:
            listacomun.append(elemento)
else:
    for elemento in lista2nr:
        if elemento in lista1nr:
            listacomun.append(elemento)
for i in range(len(listacomun)):
    print(listacomun[i])

print("Lista de nombres de 1° que no se repiten en 2°: ")
for elemento in lista1nr:
    if elemento not in lista2nr:
        lista1nr2.append(elemento)
for i in range(len(lista1nr2)):
    print(lista1nr2[i])