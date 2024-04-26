frase = input("Ingrese una frase: ").lower()
totalv = 0
b1 = True
b2 = True
b3 = True
b4 = True
b5 = True

for i in range(0, len(frase), 1):
    if frase[i] == "a" and b1 == True:
        totalv += 1
        b1 = False
    if frase[i] == "e" and b2 == True:
        totalv += 1
        b2 = False
    if frase[i] == "i" and b3 == True:
        totalv += 1
        b3 = False
    if frase[i] == "o" and b4 == True:
        totalv += 1
        b4 = False
    if frase[i] == "u" and b5 == True:
        totalv += 1
        b5 = False

print("El total de vocales (sin repetir) en esa frase es: " + str(totalv))