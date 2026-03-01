import re
line="I AM GOOD BOY"
match=re.findall("GOOd",line)   #find all pattern
match_1=re.search("GOOD",line)
if match:
    print(match)
else:
    print(match_1)
