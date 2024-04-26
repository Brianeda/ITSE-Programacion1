frase = input("Ingrese una frase: ").lower()
totalv = 0

for i in range(0, len(frase), 1):
    if frase[i] == "a":
        totalv += 1
    if frase[i] == "e":
        totalv += 1
    if frase[i] == "i":
        totalv += 1
    if frase[i] == "o":
        totalv += 1
    if frase[i] == "u":
        totalv += 1

print("El total de vocales en esa frase es: " + str(totalv))