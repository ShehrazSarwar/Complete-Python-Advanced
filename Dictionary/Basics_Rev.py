mydict = {"name":"Max","age":22,"city":"new york"}
print(mydict)

# Another way to define a dictionary
mydict2 = dict(name ="Max",age = 28,city = "new york")
print(mydict2)

print(mydict.pop("name")) # Remove name only
print(mydict)
print(mydict2.popitem()) # remove the last key
print(mydict2)