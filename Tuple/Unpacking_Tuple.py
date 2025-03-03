# we can assign tuple to variables

mytuple = ("James","Ronald","Larry")
cat1,cat2,cat3 = mytuple
print(cat1,cat2,cat3)

# this mean we can also return three different values or a tuple from a function also

mytuple = (1,2,3,4,5)
i1,*i2,i3 = mytuple
print(i1)
print(i2)
print(i3)

# Here i2 will contain the rest of the tuple elements except start and last one
# we did this by use of asterik *