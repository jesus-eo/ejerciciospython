def one_list(lst):
    x = []
    for i in lst:
        x.extend(i)
    return x



print(one_list([[1, 2], [3, 4]]))
