#Volume of sphere
def vol(rad):
    return (4.0/3)*(3.14)*(rad**3)
result = vol(4)
print("result is ....",result)


#Range check function
def ran_check(num,low,high):
    return num in range(low,high+1)

check_res = ran_check(5,4,7)
print("check_res",check_res)


#Upper case and lower case string
def up_low(s):
    check={"upper":0, "lower":0}
    for data in s:
        if data.isupper():
            check["upper"]+=1
        elif data.islower():
            check["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", check["upper"])
    print("No. of Lower case Characters : ", check["lower"])

up_low_check = up_low("Hello Elsa. Nice to MeeT yoU")
# print("up_low_check....",up_low_check)


#Unique number
def unique_list(l):
    data_list = []
    for data in l:
        if data not in data_list:
            data_list.append(data)
    return data_list
unique_check = unique_list([1,5,3,3,3,4,5,6,6,7,3,6])
print("unique_check...",unique_check)


#Multiply all numbers
def multiply(numbers):  
    total = 1
    for data in numbers:
        total *= data 
    return total 
print("multiply numbers...",multiply([1,2,3,4,5]))


#Palindrome check 
def palindrome(s):
    
    s = s.replace(' ','') # This replaces all spaces " " with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1] # Check through slicing
print("Palindrome....",palindrome("hellehq"))


#Pangram check
import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())  
print("isPangram.....",ispangram("hello"))