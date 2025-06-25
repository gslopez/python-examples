dic = {
    "name": "gonzalo",
    "age": 30,
    "city": "Chile",
    "country": "Chile",
}


# Forma 1
print('-----------')
print(dic)

# Forma 2
print('-----------')
for key in dic.keys():
    print(key, dic[key])

# Forma 3 (values only)
print('-----------')
for value in dic.values():
    print(value)

# Forma 4 (todo de una)
print('-----------')
for key, value in dic.items():
    print(key, value)

