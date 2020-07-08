import json
import re

# convert python objects into json
print(json.dumps({"fruit":"apple", "vegetable":"potato"}))  # dictionary #
print(json.dumps(("csv", "ve0", "616")))                    # tuple #
print(json.dumps(["13", "egw", "4842"]))                    # list #
# print(json.dumps({"ew2", "879e"}))                          # set #
print(json.dumps("String"))                                 # String #
print(json.dumps(48))                                       # int #
print(json.dumps(45.26))                                    # float #
print(json.dumps(True))                                     # boolean #
print(json.dumps(None))                                     # None #


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=2))

# regular expression
txt = "today is tuesday in India"
x = re.search("^today.*India$", txt)

if x:
    print("true")
else:
    print("false")

# findall
text = "Need to find all expressions"
x = re.findall("ee", text)
y = re.findall("wsa", text)
print(x)
print(y)

# search
sea = "i am here to search"
m = re.search("\s", sea)
print("1st white: ", m.start())

# split
p = re.split("\s", sea)
print(p)

# sub
ui = re.sub("\s", "=", sea)
print(ui)

