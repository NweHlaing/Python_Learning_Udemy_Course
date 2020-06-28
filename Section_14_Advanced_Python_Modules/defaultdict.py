from collections import defaultdict

d = {}
# d['one']
# print("d value....",d['one'])
d  = defaultdict(object)
d['one']
print("d value....",d['one'])

for item in d:
    print(item)

d = defaultdict(lambda: 0)
d['one']
#assign value
d['one'] = 300
print("d lambda.....",d['one'])

#print wrong value
print("d lambda.....",d['two'])

