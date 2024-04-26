año = int(input("Ingrese un año: "))

if año%4 == 0 and año%100 != 0:
    if año%400 == 0:
        print("No es un año bisiesto")
    else:
        print("Es un año bisiesto")
else:
    print("No es un año bisiesto")