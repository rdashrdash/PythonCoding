print('Hello World')
print(4*5)
print(55-44)

#Take user keyboard input
name = "Rupesh"
print("Hello " + name)

#SplitLine
splStr = "How\nis\nthe\njosh!"
print(splStr)

#Tabbed string
tabStr = "1\t2\t3\t4"
print(tabStr)

#Get specific position values
print('Man'[1])
print('bpy'[2])

print('education'[2:5])
print('education'[2:])
print('education'[:5])

print('education'[2:6:2])

guess = int(input("Your choice: "))
benchmark = 10

if guess > benchmark:
    print('Greater')
elif guess < benchmark:
    print('Smaller')
else:
    print('Equal')

tree1='ram'
tree2='sham'
if tree1 == tree2:
    print("Equal")
else:
    print("Check")