def chocolateria(cantidad):
    if cantidad % 5 == 0:
        return "Se lo puede llevar en " + str(cantidad // 5) + " cajas de 5 unidades"
    if cantidad % 8 == 0:
        return "Se lo puede llevar en " + str(cantidad // 8) + " cajas de 8 unidades"
    if cantidad % 13 == 0:
        return "Se lo puede llevar en " + str(cantidad // 13) + " cajas de 13 unidades"

    total_13 = cantidad // 13
    for i in range(total_13, -1, -1):
        remaining = cantidad - i * 13
        if remaining % 5 == 0:
            return "La cantidad de cajas de 13 unidades es " + str(i) + " junto con " + str(remaining // 5) + " cajas de 5 unidades"
        if remaining % 8 == 0:
            return "La cantidad de cajas de 13 unidades es " + str(i) + " junto con " + str(remaining // 8) + " cajas de 8 unidades"

    return "No se puede distribuir cajas para completar este pedido"

print(chocolateria(7894))