# We can also convert a single list or an iterable into a tuple

mytuple = tuple(["larry","James","Ronald"])
print(mytuple)

# tuple of lists

mytuple = (["Larry",2],["James",5],["Ronald",1])
print(mytuple)

# what if we try to change the list inside the tuple?
# changing the list inside a tuple is possilbe
mytuple[0][0] = "Baddie"
print(mytuple)

# appending into a list inside a tuple is possible
mytuple[0].append("bad")
print(mytuple)

# access through index is also possible
print(mytuple[2][0])

# But we can't modify tuple itself
# mytuple[0] = ["jkames",5]
# we can convert tuple to list and then back to tuple if we want to do some changes to a tuple