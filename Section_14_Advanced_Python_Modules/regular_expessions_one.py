text = "The person's phone number is 408-555-1234. Call soon!"
print('phone' in text)

import re
pattern = 'phone'
print("pattern one",re.search(pattern,text))
pattern = "NOT IN TEXT"
print("pattern two",re.search(pattern,text))
pattern = 'phone'
match = re.search(pattern,text)
print("Match.....",match)
print("span",match.span())
print("Start...",match.start())
print("end...",match.end())

################################
text = "my phone is a new phone"
match = re.search("phone",text)
print("match",match.span())
matches = re.findall("phone",text)
print("find all....",matches)
print("Find all length...",len(matches))


for match in re.finditer("phone",text):
    print(match.span())

print("Group....",match.group())