print("Ingrese un día de la semana: ")
dia = input()
if dia == "Lunes":
    print("El día es Lunes")
elif dia == "Viernes":
    print("El día es Viernes")
elif dia == "Sabado" or dia == "Domingo":
    print("El día puede ser Sábado o Domingo")
else:
    print("El día puede Martes, Miércoles o Jueves")