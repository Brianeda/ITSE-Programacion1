def es_bisiesto(anio):
    """
    Verifica si un año es bisiesto.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def main():
    anio_inicio = int(input("Ingrese el año de inicio: "))
    anio_fin = int(input("Ingrese el año de fin: "))

    print("Años bisiestos y múltiplos de 10 en el rango de", anio_inicio, "a", anio_fin, ":")

    for anio in range(anio_inicio, anio_fin + 1):
        if es_bisiesto(anio) and anio % 10 == 0:
            print(anio)

if __name__ == "__main__":
    main()