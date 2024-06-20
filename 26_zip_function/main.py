array1 = [1,2,3,4,5] ##If the two arrays are not equal dimension then it will take the smaller one 
array2 = [10,20,30,40,50]

for i in zip(array1,array2):
    print(i)


for i,j in zip(array1,array2):
    print(i,j)


