nums = [1,1,1,2,3,3,3,4,5,6,2,1,2,1,2,7,6,4,8,9,10,10]


#@ 1.1
mySet1 = set()
for n in nums:
    mySet1.add(n)
print(mySet1)


#@ 1.2
mySet2 = {n for n in nums}
print(mySet2)