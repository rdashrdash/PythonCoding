from CodingRules import Hello


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myFunc()


class Try:
    def __init__(self, name, school):
        self.name = name
        self.school = school

    def fun(self):
        print("my name is " + self.name)


q1 = Try("Rupesh", 11)
q1.fun()

q1.school = 22
print(q1.school)

mytuple = ("q", "w", "e")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


mystr = "rupesh"
myread = iter(mystr)

print(next(myread))

string = "dash"
for x in string:
    print(x)


class MyNumber:
    def __iter__(self):
        self.a = 2
        return self

    def __next__(self):
        if self.a <= 20:
            y = self.a
            self.a += 2
            return y
        else:
            raise StopIteration


cla = MyNumber()
itr = iter(cla)

for y in itr:
    print(y)


print(Hello.bikes)

a = Hello.train[2]
print(a)


details = {"as":42, "ed":52, "rf":69, "fv":91}
