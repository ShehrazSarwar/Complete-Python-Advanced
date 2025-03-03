# Copy list

# without copy() function:
mylist = [5] * 3
print(mylist)

mylist2 = mylist # Called reference copy
mylist2.append(25)

print(mylist)
print(mylist2)

print()
# withcopy function:
mylist = [5] * 3
print(mylist)

mylist2 = mylist.copy() # make a copy of itself
mylist2.append(25)

print(mylist)
print(mylist2)

# Some Revisions of these two here
print(mylist.index(5))  # returns the first occurance index
print(mylist.count(5))  # counts the number of times