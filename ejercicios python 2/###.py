def histogram(lst, char):
    x = []

    for i in lst:
        x.append(i * char + '\n')
    return "".join(x)

print(histogram([2, 5, 6, 10], "#"))
