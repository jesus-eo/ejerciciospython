def isograma(palabra):
    palabra = palabra.lower()
    acc = 0

    while acc < len(palabra):
        x = palabra[acc]
        if x in palabra:
            acc += 1
    return acc > 1









print(isograma('manol'))
