'''(["1=one", "2=two", "3=three", "4=four"])'''
'''def str_dic(lst):
     x = tuple(lst)
     y = dict(x)
     return x
print(str_dic((["1 = one", "2 = two", "3 = three", "4 = four"])))'''

def str(lst):
    for k, v in lst.items():
        return k

print(str((["1 = one", "2 = two", "3 = three", "4 = four"])))
