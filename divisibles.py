# primero definimos la funcion deff 
def divisibleX5(lista):
    res = []
    i = 0
    #creamos un bucle con el comando while
    while i < len(lista):
        if lista[i] % 5 == 0:
            res.append(lista[i])
        i += 1
    #usamos la variable return para devolver el valor
    return res
