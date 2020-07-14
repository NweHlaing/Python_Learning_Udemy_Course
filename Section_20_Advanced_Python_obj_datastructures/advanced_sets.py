s = set()

#Add
s.add(1)
s.add(2)
print("s....",s)

#clear
s.clear()
print("Clear....",s)

#Copy
s = {1,2,3}
sc = s.copy()
print("Copy....",sc)
print("original s...",s)
s.add(4)
print("s after 4 add..",s)
print("copy s..",sc)

#Difference
print("diff s and sc..",s.difference(sc))

#Difference update

s1 = {1,2,3}
s2 = {1,4,5}
diff = s1.difference_update(s2)
print("s1 after diff..",diff)

#Discard
print("s before dis..",s)
s.discard(2)
print("s after disc..",s)


#intersection and intersection_update
s1 = {1,2,3}
s2 = {1,2,4}
print("interset s1 and s2..",s1.intersection(s2))
print("s1 after intersetion..",s1)

s1.intersection_update(s2)
print("s1 after intersetion update..",s1)

#isdisjoint
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
print("s1 disjoint s2...",s1.isdisjoint(s2))
print("s1 disjoint s3...",s1.isdisjoint(s3))


#issubset
print("s1 in subset...",s1)
print("s2 in subset...",s2)
print("s1 and s2 sbuset..",s1.issubset(s2))

#issuperset
print("s1 and s2 superset..",s2.issuperset(s1))
print("s1 and s2 superset..",s1.issuperset(s2))

#symmetric_difference
print("s1 in sys_dif...",s1)
print("s2 in sys_dif...",s2)
print("s1 and s2 symmetric difference...",s1.symmetric_difference(s2))

#union
print("s1 and s2 union...",s1.union(s2))

#update
s1.update(s2)
print("s1 and s2 update...",s1)