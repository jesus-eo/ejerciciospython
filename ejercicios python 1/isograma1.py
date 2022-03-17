def isograma(palabra):

    palabra = palabra.islower()
    palabra1 = list(palabra)
    acc = 0

    while acc < len(palabra1):
        x = palabra1[acc]
        if palabra1.count(x) > 1:
            True
        else:
            acc+=1
    return False

print(isograma('hola'))
