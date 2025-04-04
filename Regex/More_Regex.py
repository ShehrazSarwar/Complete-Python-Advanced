import re

txt = "afaga;qfawdf;awd2--"

# let's say I have to extract only alphabets from the string
# for except we use [^any_character]

pattern = "[^;-]"  # ^ ---> except
print(re.findall(pattern,txt))

# To match all digits or something like below
txt = "According to data today's sale is $4.85 and previous sale was $3"

pattern = r"\$[\d\.]+"   # I am using \ here with dollar to exactly match it or [0-9\.]+
# because dollar sign has a special meaning of ending of a string
# + means one or more and . is again a special character so put \ before it!
# here I put [] why? it is because I want to match one more only the digits
print(re.findall(pattern,txt))

# let's print only number not dollar sign

pattern = r"\$([\d\.]+)"  # () have a special meaning of group, meaning that It will only extract data
# written inside the (_) starting from dollar $ sign
print(re.findall(pattern,txt))