fecha = input("Ingrese la fecha en formato (día, DD/MM): ")

DD = int(str(fecha[-5])+str(fecha[-4]))
MM = int(str(fecha[-2])+str(fecha[-1]))

aux = 0
dia = ""

while fecha[aux] != ",":
    dia = dia + fecha[aux]
    aux += 1

dia = dia.lower()

i = 0

if dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves" or dia == "viernes" or dia == "sabado" or dia == "domingo":
    if DD <= 31:
        if MM <= 12:
            nivel = input("Ingrese su nivel: ").lower()
            if nivel == "inicial" or nivel == "intermedio" or nivel == "avanzado":
                examen = input("Ese día hubo examen? (si/no): ").lower()
                if examen == "si":
                    aprobados = int(input("Ingrese la cantidad de aprobados: "))
                    desaprobados = int(input("Ingrese la catidad de desaprobados: "))
                    total = 100/(aprobados+desaprobados)*aprobados
                    print("El porcentaje de aprobados fue: %" + str(total))
            elif nivel == "viajero":
                if dia == "jueves":
                    asistencia = int(input("Ingrese el porcentaje de asistencia a prácticas habladas: "))
                    if asistencia > 50:
                        print("Asistió la mayoría")
                    else:
                        print("No asistió la mayoría")
                elif dia == "viernes" and DD == 1 and (MM == 1 or MM == 7):
                    print("Comienzo de nuevo ciclo")
                    nciclo = input("Ingrese la cantidad de alumnos en el nuevo ciclo: ")
                    arancel = input("Ingrese el arancel por alumno: ")
                    print("El ingreso total de aranceles fue de $" + str(int(arancel)*int(nciclo)))
        else:
            print("Se produjo un error.")
    else:
        print("Se produjo un error.")
else:
    print("Se produjo un error.")