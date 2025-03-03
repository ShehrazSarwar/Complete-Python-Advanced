# Copy
mydict = {"name":"Max","age":22,"city":"new york"}
print(mydict)

# Another way to define a dictionary
# mydict2 = mydict   #---> eference Copy
mydict2 = mydict.copy() # or mydict2 = dict(mydict)
mydict2["email"] = "Xyz@gmail.com"
print(mydict2)
print(mydict)
