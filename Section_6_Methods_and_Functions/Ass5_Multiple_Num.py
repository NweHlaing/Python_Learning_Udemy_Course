#Multiply all numbers
def multiply(numbers):  
    total = 1
    for data in numbers:
        total *= data 
    return total 
print("multiply numbers...",multiply([1,2,3,4,5]))