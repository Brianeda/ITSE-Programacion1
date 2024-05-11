frase = input("Ingrese una frase: ").lower()
atotal = 0
etotal = 0
itotal = 0
ototal = 0
utotal = 0

for i in range(0, len(frase), 1):
    if frase[i] == "a" or frase[i] == "á":
        atotal += 1
    if frase[i] == "e" or frase[i] == "é":
        etotal += 1
    if frase[i] == "i" or frase[i] == "í":
        itotal += 1
    if frase[i] == "o" or frase[i] == "ó":
        ototal += 1
    if frase[i] == "u" or frase[i] == "ú":
        utotal += 1

print("Cantidad de ocurrencias de la vocal A: " + str(atotal))
print("Cantidad de ocurrencias de la vocal E: " + str(etotal))
print("Cantidad de ocurrencias de la vocal I: " + str(itotal))
print("Cantidad de ocurrencias de la vocal O: " + str(ototal))
print("Cantidad de ocurrencias de la vocal U: " + str(utotal))