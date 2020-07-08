import platform
from CodingRules.Reference import details
import datetime
import json

# using import
x = platform.system()
print(x)

# directory of platform library
y = dir(platform)
print(y)

# getting data from other modules
print(details["as"])

# date time
s = datetime.datetime.now()
print(s)
print(s.day)
print(s.microsecond)
# Day
print(s.strftime("%A"))

z = datetime.datetime(2005, 11, 30)
# month
print(z.strftime("%B"))
print(z.strftime("%A"))
# year short form
print(z.strftime("%y"))


# json is syntax for storing & exchanging data
d = '{"sq":"e55wwe", "efw":"5w5dw", "efw":"156dww"}'
# convert json to python
e = json.loads(d)
print(e["sq"])

# convert python into json
py = {"name":"rupesh", "age":"28", "place": "bls"}
js = json.dumps(py)
print(js)

