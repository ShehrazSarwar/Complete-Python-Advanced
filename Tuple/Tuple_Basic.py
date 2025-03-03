mytuple = ("larry",50,"James")
print(mytuple)

# also a tuple if assigning multiple values to a single variable
mytuple = "larry",50,"James"
print(mytuple)

# not a tuple
mytuple = ("larry")
print(mytuple)

# in-order to add sinle element in a tuple seperate it by a comma
mytuple = ("larry",)
print(mytuple)

# Some revision of methods of Tuple here:
print(mytuple.count("james"))  # will return zero since there is no james

mytuple = ('a','p','p','l','e')
# print(mytuple.index('n')) # Value error
print(mytuple.index('l'))

# slicing is also possible like lists and strings
print(mytuple[1:])
print("Revered: ",mytuple[::-1])