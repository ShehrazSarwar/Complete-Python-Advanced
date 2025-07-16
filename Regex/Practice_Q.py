# Q) Extract Tesla's Financial Period & It's Cost
import re

txt = """
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 
billion. In previous quarter i.e. 
FY2020 Q4 it was $3 billion.
"""

pattern = r"FY(\d{4} Q[1-4])[^\$]+\$([0-9\.]+)"
# [^\$] upto but not included!
print(re.findall(pattern,txt))