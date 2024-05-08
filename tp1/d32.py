def potencia(n, x):
    if x == 1:
        return n
    else:
        total = n
        aux = n
        for i in range(x - 1):
            temp = 0
            for j in range(n):
                temp += total
            total = temp
        return total

print(potencia(5, 5))