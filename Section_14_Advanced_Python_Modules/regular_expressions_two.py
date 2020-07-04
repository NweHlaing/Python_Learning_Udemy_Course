import re
#Pattern
text = "My telephone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print("Group...",phone.group())
search = re.search(r'\d{3}-\d{3}-\d{4}',text)
print("Search....",search)

#Group
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
# The entire result
print("Result....",results.group())
print("Result 1...",results.group(1))
print("Result 2...",results.group(2))
print("Result 3...",results.group(3))

#Additional Reg Syntax
#Or Operator
man_or = re.search(r"man|woman","This man was here.")
print("or....",man_or)
woman_or = re.search(r"man|woman","This woman was here.")
print("woman...",woman_or)


#Wildcard operator
wild_find = re.findall(r".at","The cat in the hat sat here.")
print("wild_find all.....",wild_find)
wild_two = re.findall(r".at","The bat went splat")
print("Wild two find...",wild_two)
wild_three = re.findall(r"...at","The bat went splat")
print("Wild three find...",wild_three)

# One or more non-whitespace that ends with 'at'
wild_four = re.findall(r'\S+at',"The bat went splat")
print("Wild four...",wild_four)

# Ends with a number
wild_five = re.findall(r'\d$','This ends with a number 2')
print("Five...",wild_five)

# Starts with a number
wild_six = re.findall(r'^\d','1 is the loneliest number.')
print("six.....",wild_six)

#Exclusion
phrase = "there are 3 numbers 34 inside 5 this sentence."
print("all",re.findall(r'[^\d]',phrase))
print("phrase",re.findall(r'[^\d]+',phrase))

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print("test phrase...",re.findall('[^!.? ]+',test_phrase))