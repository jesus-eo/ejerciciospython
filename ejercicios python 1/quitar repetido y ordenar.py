'''unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]'''

def organize(lst):
    x = set(lst)
    y = list(x)
    cont = (1)
    alma = []
    for l in y:
        if l > y[cont]:
            alma.append(l)
            cont += 1
        else:
            alma.extend(l)


    return alma


print(organize([1, 3, 4, 4, 4, 5, 6, 100, 27]))
