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
# difinimos los numeros para sacarles los divisibles 
numeros = [5,9,10,14,15,25,29,35,40]
divisibles = divisibleX5(numeros)
print(divisibles)
