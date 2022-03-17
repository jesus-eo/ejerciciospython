def isograma(palabra):
    ''' letra repetida'''
    m = palabra.lower()
    p = m.replace(' ', '')

    s = set(p)



    return len(s) >= len(p)



print(isograma('camino'))
