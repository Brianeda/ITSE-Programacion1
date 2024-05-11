import math
pi = math.pi

opc = ""

print("                   Menú de Opciones")
print("-----------------------------------------------------------")
print("1 - Calcular volumen contenedor rectangular")
print("2 - Calcular volumen contenedor redondo")
print("3 - Calcular volumen contenedor cilíndrico")
print("s - Salir")
print("-----------------------------------------------------------")
while opc != "1" and opc != "2" and opc != "3" and opc != "s":
    opc = input()
    if opc != "1" and opc != "2" and opc != "3" and opc != "s":
        print("OPCIÓN NO VÁLIDA")


print("DATOS DEL CONTENEDOR")
if opc == "1":
    alto = float(input("Ingrese el alto: "))
    ancho = float(input("Ingrese el ancho: "))
    largo = float(input("Ingrese el largo: "))
    resp = alto * ancho * largo
    print("Volúmen en litros: " + str(resp))
elif opc == "2":
    radio = float(input("Ingrese el radio: "))
    resp = radio / 2
    print("Volúmen en litros: " + str(resp))
elif opc == "3":
    radio = float(input("Ingrese el radio: "))
    alto = float(input("Ingrese el alto: "))
    resp = volumen = pi * radio ** 2 * alto
    print("Volúmen en litros: " + str(resp))