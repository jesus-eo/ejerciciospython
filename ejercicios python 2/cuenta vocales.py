def count_vowels(txt):
     x = ['a', 'e', 'i', 'o', 'u']

     y = len([s for s in txt if s in x])
     return y



'''def count_vowels(txt):
     x = ['a', 'e', 'i', 'o', 'u']
     cont = 0
     for s in txt:
         if s in x:
             cont +=1
     return cont'''
print(count_vowels("lssdeeama"))
