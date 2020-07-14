s = 'hello world'

#change case
print("Capital case",s.capitalize())
print("Upper case",s.upper())
print("Lower case",s.lower())


print("count o...",s.count('o'))
print("find o...",s.find('o'))

#Formatting
print(s.center(20,'z'))

#isCheck
s = 'hello'
#alphanumeric
print("alnum",s.isalnum())
#alphabetic
print("alphabet",s.isalpha())   
#lower
print("lower",s.islower())   
#space
print("space",s.isspace())  
#title
print("title",s.istitle()) 
#upper
print("upper",s.isupper())    
#endswith
print("end with",s.endswith('o'))

#split
print("split e",s.split('e'))
print("split l",s.partition('l'))

