'''count_all("Hello World") ➞ { "LETTERS":  10, "DIGITS": 0 }'''
def count(txt):
    letras = len([x for x in txt if x.isalpha()])
    digit = len([x for x in txt if  x.isdigit()])
    a = {}
    a["LETTERS"] = letras
    a["DIGITS"] = digit
    return a
    
    
print(count("Helff2222lo World"))