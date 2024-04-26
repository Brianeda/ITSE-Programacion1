aux = True

print("Ingrese una vocal: ")
vocal = input().lower()


while aux == True:
    if len(vocal) == 1:
        if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
            print("Es vocal")
        aux = False
    else:
        print("Debe ingresar sólo un carácter. Reingresar:")
        vocal = input().lower()

