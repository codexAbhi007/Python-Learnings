arr = [1,2,3,4,5,6]

def cube(x):
    return x**3

## AAM zindagi
# newl = []
# for i in arr:
#     newl.append(cube(i))
# print(newl)

##Mentos zindagi

newl = map(lambda x:x**2,arr)
print(newl) #@Returns a map object
print(type(newl)) #@class map
print(list(newl))

print(list(map(cube,arr)))
print(arr)

#!Map func doesnot change the original list

