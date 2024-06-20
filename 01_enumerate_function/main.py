marks = [12,56,24,54,54,98,45]
import pandas as pd
print(pd.__version__)

#@Traditional way
# index = 0 
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("Awesome")
#     index += 1 


#@Enumerate Function

for index, mark in enumerate(marks): 
    print(mark)
    if (index == 3):
        print("Awesome")


fruits = ["Apple","Banana","Mango"]

enu = enumerate(fruits)

print(enu) #~Returns an Enumerate class
print(type(enu))
print(list(enu)) ## List of tuples with first index then item
for index, fruit in enumerate(fruits,start=1): ##Index will start from 1
    print(index, fruit)