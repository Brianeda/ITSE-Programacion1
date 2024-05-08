def case1():
    return "Usted votó por el partido Rojo"

def case2():
    return "Usted votó por el partido Verde"

def case3():
    return "Usted votó por el partido Azul"

def eleccion(case):
    return switch.get(case, lambda: "Participante no válido")()

switch = {
    "A": case1,
    "B": case2,
    "C": case3,
}

print("Ingrese el candidato al que quiere votar: ")
case = str(input().upper())
print(eleccion(case))