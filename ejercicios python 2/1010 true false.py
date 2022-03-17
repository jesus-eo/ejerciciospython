'''integer_boolean("100101") ➞ [True, False, False, True, False, True]

integer_boolean("10") ➞ [True, False]'''

'''def integer_boolean(n):
    x = []
    for s in n:
        if s == '1':
            x.append(True)
        else:
            x.append(False)
    return x'''

def integer_boolean(n):
   return [s == '1' for s in str(n)]



print(integer_boolean('10'))
