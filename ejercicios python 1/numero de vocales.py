def vocales(cadena):

  letras = ['a', 'e', 'i', 'o', 'u']
  return len([s for s in cadena if s in letras])



print(vocales('haloal'))
