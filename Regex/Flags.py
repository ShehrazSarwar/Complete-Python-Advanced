import re

txt = "The rain in SPAIN"

#Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall("spain", txt,re.IGNORECASE))
#re.I or re.IGNORECASE