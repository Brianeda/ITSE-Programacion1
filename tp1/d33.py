prueba = [1, 2, 3, 4, 5]

def nlista(olista):
    nlista = []
    for i in olista:
        nlista.append(i)
    for i in range(len(nlista)):
        nlista[i] = nlista[i] + 1
    return nlista

print(nlista(prueba))