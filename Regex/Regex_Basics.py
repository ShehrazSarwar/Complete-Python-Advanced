import re

txt = """
Follow our leader Elon musk Number 9991116666 on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news, 40
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
Tesla's USA No- (999)-333-7777
"""

# Since we have a special meaning of special character \ --> (use for escape sequences)
# The solution is to use Python’s raw string notation for regular expression patterns
# Inorder to let compiler know that don't check for any syntax error for \ or \\

pattern = r"\d{10}|\(\d{3}\)-\d{3}-\d{4}"
# here \d used to check for any digit and {Any Count} for more than one count checking!
print(re.search(pattern,txt))  # return starting and ending index position with match pattern

matches = re.findall(pattern,txt)  # return list of all possible matched found from the string
print(*matches)