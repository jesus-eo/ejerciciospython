'''Cree una función que tome una lista que contenga listas anidadas como argumento. Cada sublista tiene 2 elementos. El primer elemento es el numerador y el segundo elemento es el denominador. Devuelve la suma de las fracciones redondeadas al número entero más cercano.'''
import math
def sum_fractions(lst):
    division = []

    for i in lst:
        division.append(i[0] // i[1])

    return division



print(sum_fractions(([[18, 13], [4, 5]])))
