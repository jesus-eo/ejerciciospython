'''def reverse(lst):

    if lst == 0:
        return "boolean expected"
    elif lst == True:
        return False
    elif lst == False:
        return True

    else:
        return "boolean expected"'''


'''reverse(True) ➞ False

reverse(False) ➞ True

reverse(0) ➞ "boolean expected"

reverse(None) ➞ "boolean expected"'''

def reverse(arg):
	if type(arg) != bool:
		return "boolean expected"
	return not arg

print(reverse(True))
