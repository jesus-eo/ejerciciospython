def palindromo(datos):
    datos = datos.lower()
    datos_x = []
    cont = 0

    while cont < len(datos):
        if datos[cont].isalpha():
            datos_x.append(datos[cont])
        cont += 1
    datos_p = datos_x[::-1]
    return datos_x == datos_p
print(palindromo('hola, que tal'))
