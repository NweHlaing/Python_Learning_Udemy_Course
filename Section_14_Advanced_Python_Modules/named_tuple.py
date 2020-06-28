t = (12,13,14)
print("Data in zero",t[0])

from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])
sam = Dog(age=2,breed='Lab',name='Sammy')
frank = Dog(age=2,breed='Shepard',name="Frankie")

print("Sam....",sam)
print("Sam's Age...",sam.age)
print("Sam's Breed...",sam.breed)
print("Sam's Name...",sam.name)
print("Sam's zeor data...",sam[0])