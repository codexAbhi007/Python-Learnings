from math import sqrt,floor
# from main2 import multiply
import main3 
def sqrt(a,b): #!This will overwrite the imported functions     
    return(a-b)

result = sqrt(9,2)
print(result)
print(floor(454.23453))


# r = multiply(5,6)
# print("THIS IS IMPORTED FROM ANOTHER FILE AND THE RESULT IS ",r)

r = main3.eigen()
print(r)


