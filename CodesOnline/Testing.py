print("mul" * 2)

name  = 'Rupesh'
greet = f"Hi, {name}"
print(greet)
print(f"Hi, {name}")

say = "Hi, {}"
with_name = say.format("Rahul")
print(with_name)

welcome = "Welcome {} to {}"
final = welcome.format("Kat", "India")
print(final)

# name = input("enter name: ")
# print(name)
# age = int(input("Age please: "))
# print(age)
# print("{} is {} years old".format(name, age))
# print(f"{name} is {age} years old")

# list by []
li = ["q", "f", "m"]

# tuple by ()
tup = ("re", "pe", "se")

# sets by {}. Can add and remove. No duplicate element.
st1 = {"der", "mic", "swl"}
st2 = {"kim", "rim", "mic", "der"}

# modification in list
li[2] = "k"
li.append("g")
print(li)

# set modification
st1.add("wis")
print(st1)
uni = st1.union(st2)
print(uni)
dif = st1.difference(st2)
print(dif)
inter = st1.intersection(st2)
print(inter)

sre = {5}
sre.add(6)
sre.add(7)
print(sre)

lo = [12, 34, 23]
print(lo)
tu = 32, 45, 67
print(tu)

if st2 in st1:
    print('Yes')
else:
    print('Not')

# Dictionaries
stu_ade = {"Rah": 45, "Mak": 78, "rei": 49}

for student, attendance in stu_ade.items():
    print(f"{student} : {attendance}")
print(list(stu_ade.items()))


def para(who):
    print(f"Hi {who}")


para('Tim')


users = [(0, "Si", "pw"), (1, "WSewvw", "hDJWNk"), (2, "iwcnj", "Hbwjcjk")]
u_map = {users[1]: user for user in users}
u_inp = input("username")
u_pwd = input("passw")

_, username, password = u_map[u_map]

if u_pwd == password:
    print("Success")
else:
    print("Fail")
