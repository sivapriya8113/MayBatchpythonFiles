# import json
#
# # some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'
# print(type(x))
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y)
#
# print(type(y))

"""
json - storing nd exchanging of data

"""
import json

# some JSON:
# x = { "name":"John", "age":30, "city":"New York"}
# print(type(x))
# # parse x:
# y = json.dumps(x)
#
# # the result is a Python dictionary:
# print(y)
# print(type(y))

import random
print(random.randint(1, 10) * 7)

s = "python"
print(random.choice(s))

color = "#%06x" % random.randint(0,0xfffff)
print(color)



import json # javascript object notation

# x = {'name':'priya','age':12,'course':'python'}
# print(type(x))
# y = json.dumps(x) # python to json
# print(y)
# print(type(y))
#
# x = '{"name":"priya","age":12,"course":"python"}'
# print(type(x))
# y = json.loads(x) # json to python
# print(y)
# print(type(y))
# print(y['age'])


import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
y = json.loads(sampleJson)
# print(y['company']['employee']['payble']['salary'])


# func = dir(json)
# print(func)
# import os
# print(dir(os))
#
