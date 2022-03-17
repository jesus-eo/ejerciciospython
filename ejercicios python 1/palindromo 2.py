def palindromo(datos):
    datos = datos.lower()
    datos_p = []
    cont = 0

    while cont < len(datos):
        y = (datos[cont])
        if y.isalpha():
            datos_p.append(y)
        cont += 1
    datos_b = datos_p[::-1]

    return datos_b == datos_p

print(palindromo('amar da drama'))
