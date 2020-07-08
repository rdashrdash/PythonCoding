first = 'this is first statement'
second = 'this is second statement'
entry = 'this is'

if entry in first:
    print("{} is available inside {}.".format(entry, first))
else:
    print("try again")

for i in range(0, 10, 3):
    print(i)

shop_list = ['milk', 'book', 'tea', 'curd']
for item in shop_list:
    print(item)

check = 'TEA'
pos = None
for j in range (len(shop_list)):
    if shop_list[j] == check.casefold():
        pos = j
        break
print("found at {} ".format(pos))

# i = 0
# while i<10:
#     print(i)
#     i += 1

r = range(0, 10)
for i in r[::-1]:
    print(i)