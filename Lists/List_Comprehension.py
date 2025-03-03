mylist = [1,2,3,4,5]
newlist = [x*x for x in mylist]
print(newlist)

newlist = [x for x in mylist if x % 2 == 0]
print(newlist)