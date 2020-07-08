print("Welcome")

def fun():
    print("function")
fun()

def argu(arg):
    print(arg + "ument")
argu("arg")

x=int(0)
if x<0:
    print("negative")
elif x>0:
    print("positive")
else:
    print("zero")

print(range(10))

for n in range(3, 11):
    for x in range(2, n):
        if n%x == 0:
            print(n, "is a composite number")
            break
    else:
        print(n, "is a prime number")

bikes = ["ninja", "bullet", "ducati"]
a = bikes[2]
print(a)
b = len(bikes)
print(b)
for a in bikes:
    print(a)
bikes.append("luna")
print(bikes)
bikes.remove("luna")
print(bikes)
bikes.insert(2, "vespa")
print(bikes)
bikes.sort(reverse=False)
print(bikes)


def sortlist(w):
    return len(w)
cars = ["audi", "bmw", "mercedies", "jaguar"]
cars.sort(key=sortlist)
print(cars)
q=cars.count("bmw")
print(q)

cars.extend(bikes)
print(cars)

train= (1, 5, 9, 3, 7)
bikes.extend(train)
print(bikes)

