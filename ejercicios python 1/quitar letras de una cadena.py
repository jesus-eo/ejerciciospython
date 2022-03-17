def numero(lst):
    x = list(lst)
    return [i for i in x if  type(i) is int]
print(numero([1, 2, "a", "b"]))


def filter_list(lst):
  all_num = []

  for i in lst:
    if type(i) == int:
      all_num.append(i)
    else:
      pass
  return all_num
