list1 = [1,2,3]

#append
list1.append(4)
print("list after appand..",list1)

#count
count = list1.count(10)
count1 = list1.count(2)
print("list count..",count)
print("list count 1..",count1)

#append and extend
x = [1, 2, 3]
x.append([4, 5])
print("append...",x)

x = [1, 2, 3]
x.extend([4, 5])
print("extend...",x)

#index
print("index2...",list1.index(2))


#insert
list1.insert(2,'inserted')
print("list1 after insert...",list1)

#pop
ele = list1.pop(1)
print("list1 in pop...",list1)
print("pop ...",ele)

#remove
print("list before remove...",list1)
list1.remove('inserted')
print("list after remove...",list1)
list2 = [1,2,3,4,3]
list2.remove(3)
print("list2 after remove...",list2)


#reverse
print("list2 before reverse...",list2)
list2.reverse()
print("list2 after reverse...",list2)

#sort
print("list2 before sort...",list2)
list2.sort()
print("list2 after sort...",list2)
