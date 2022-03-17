'''add_name({}, "Brutus", 300) ➞ { "Brutus": 300 }

add_name({ "piano": 500 }, "Brutus", 400) ➞ { "piano": 500, "Brutus": 400 }'''




def insertar( obj, key, value):
    obj[key] = value

    return obj
print(insertar({"piano": 500}, "Brutus", 300))
