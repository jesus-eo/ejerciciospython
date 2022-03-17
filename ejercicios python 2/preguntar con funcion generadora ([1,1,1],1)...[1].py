
'''Cree una función que tome dos argumentos: una lista lst y un número num. Si un elemento aparece en lst más de un número de veces, elimine las ocurrencias adicionales y devuelva el resultado.'''
'''delete_occurrences([1, 1, 1, 1], 2) ➞ [1, 1]

delete_occurrences([13, True, 13, None], 1) ➞ [13, True, None]

delete_occurrences([True, True, True], 3) ➞ [True, True, True]'''

'''def ocurrencias(tupla):
     resultado = []
     y = tupla[0]
     x = tupla[1]
     for i in y:
         if i not in resultado:
             resultado.append(i)
     return resultado * x
print(ocurrencias(([13, True, 13, None], 2)))'''

def  ocurrencias(tupla):
     resultado = []
     y = tupla[0]
     x = tupla[1]
     (resultado.append(i) for i in y if i not in resultado)
     return resultado

print(ocurrencias(([13, True, 13, None], 1)))
