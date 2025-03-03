# List Concatination Into A String

mylist = ['a'] * 6
print(mylist)

# Bad (more time taking)
mystring = ''
for i in mylist:
    mystring += i
print(mystring)

# Good (less time taking0
mystring = ''.join(mylist)
print(mystring)