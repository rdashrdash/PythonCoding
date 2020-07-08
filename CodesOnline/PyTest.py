# Destructuring arguments
def add(x, y):
    return x+y


nums = [3,10]
print(add(*nums))

num1 = {"x" : 12, "y" : 10}
print(add(**num1))


def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    if operator == "+":
        return sum(args)
    elif operator == "*":
        return multiply(*args)
    else:
        return "No valid operator."


print(apply(5, 6, 8, operator="*"))


# all arguments gets collected by **
def det(**qwe):
    print(qwe)


det(name="Rupesh", age="30")


# ** use
def details(name, age):
    print(name, age)


stats = {"name": "Rahul", "age": 30}

details(**stats)


