'''sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9'''
'''sum_odd_and_even([0, 0]) ➞ [0, 0])'''



def sum_odd_and_even(lst):
    pares = []
    impares = []
    for i in lst:
        if i % 2 == 0:
            pares.append(i)
        elif i % 2 != 0:
            impares.append(i)
    return [sum(pares), sum(impares)]
print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
