
# this is a dictionary with human-readable keys and values.
# usually we do this when we access the dictionary within our code.
print("Ejemplo 1")
fruits_by_name_dict = {
    "apple": "A fruit that is typically red, green, or yellow.",
    "banana": "A long, curved fruit that is yellow when ripe.",
    "cherry": "A small, round fruit that is typically red or black.",
}

print("'Apple' is ", fruits_by_name_dict["apple"])
print("'Banana' is ", fruits_by_name_dict["banana"])
print("'Cherry' is ", fruits_by_name_dict["cherry"])

print("\n")
print("Ejemplo 2")
# Dictionaries can also store data in cases where we don't know the keys in advance.
humans_by_rut_dict = {} # this will look like {"1111111-1": "Juan", "22.222.222-2": "Pedro", ...}

ruts = input("Ingresa los ruts separados por comas: ") # valid input: 11111111-1,22.222.222-2,33.333.333-3
names = input("Ingresa los nombres separados por comas: ") # valid input: Juan,Pedro,Maria
ruts_list = ruts.split(",") # transforms "11111111-1,22.222.222-2,33.333.333-3" -> ["11111111-1", "22.222.222-2", "33.333.333-3"]
names_list = names.split(",") # transforms "Juan,Pedro,Maria" -> ["Juan", "Pedro", "Maria"]

for i in range(len(ruts_list)):
    rut = ruts_list[i]
    name = names_list[i]
    humans_by_rut_dict[rut] = name
print("El diccionario de humanos es: ", humans_by_rut_dict)