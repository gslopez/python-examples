# Functions, re using logic to avoid repetition


def operation(j):
    j = j + 1
    j = j**2
    j = j / 2
    print(j)

    # return is very important. Without return, something like x = operation(x) will always result in x=None
    return j

x = int(input("Dime tu numero favorito "))
y = int(input("Dime tu segundo numero favorito "))

# operation(x) performs a series of operations on the input number
x = operation(x)
print("El resultado de tu numero favorito es: ", x)

# operation(y) performs the same series of operations, without duplicating the code
y = operation(y)
print("El resultado de tu segundo numero favorito es: ", y)










