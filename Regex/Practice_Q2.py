# Q)Extract all twitter handles from following text.
# Twitter handle is the text that appears after https://twitter.com/
# and is a single word. Also it contains only alpha numeric characters i.e. A-Z a-z , o to 9
# and underscore _

import re

text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern1 = r'https://twitter.com/(\S+)' #Or
pattern2 = r'https://twitter.com/([a-zA-Z0-9_]+)'

print(re.findall(pattern2, text))