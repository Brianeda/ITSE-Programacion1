import random

print("Piense un número entre 1.000 y 10.000")

liminf = 1000
limsup = 10000
resp = ""

while resp != "=":
    nrandom = random.randrange(liminf, limsup)
    print("El número que estás pensado es " + str(nrandom) + "?")
    resp = input()
    if resp == "<":
        limsup = nrandom
    elif resp == ">":
        liminf = nrandom
    elif resp == "=":
        print("Fácil nomás")