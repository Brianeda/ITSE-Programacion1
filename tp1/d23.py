alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

corri = int(input("Ingrese la cantidad de corrimiento: "))
m1 = ""

for i in range(5):
    mensaje = input("Ingrese el " + str(i+1) + "° mensaje a codificar: ").lower()

    for letra in mensaje:
        if letra == " ":
            m1 += " "
        elif letra in alfa:
            indice = (alfa.index(letra) + corri) % len(alfa)
            m1 += alfa[indice]

    print("Mensaje " + str(i+1) + "° codificado: " + m1)
    m1 = ""