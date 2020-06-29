#Randon numbers
import random
print("Random num....",random.randint(0,100))

# The value 101 is completely arbitrary, you can pass in any number you want
random.seed(101)
# You can run this cell as many times as you want, it will always return the same number
print("Random default",random.randint(0,100))


# The value 101 is completely arbitrary, you can pass in any number you want
random.seed(101)
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))

#random integers
print("Randon int...",random.randint(0,100))

#randon with sequences
mylist = list(range(0,20))
print("My List......",mylist)
#choice
print("My Cohice...",random.choice(mylist))
print("Random sample....",random.sample(population=mylist,k=10))


# Don't assign this to anything!
print("Shuffle....",random.shuffle(mylist))
print("My List.....",mylist)

#Random Distributions
print("Random Dis....",random.uniform(a=0,b=100))


#Normal Distribution
print("Random guss....",random.gauss(mu=0,sigma=1))





