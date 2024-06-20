a = 330000
b = 3303

print("A") if a > b else print("=") if a == b else print("B")

#Conditional assignment

c = 9 if a > b else 0 
print(c)



# syntax -> result = value_if_true if condition else value_if_false
#this is equal to 
#if condition:
#     result = value_if_true
# else:
#     result = value_if_false