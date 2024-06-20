# a = True 
# print(a=False) #@TypeError: 'a' is an invalid keyword argument for print()

print(a:=False)

n = [1,2,3,4,5]
print(n)

while(i:= len(n))>0:
    print(n.pop())

print(n)





##AAM ZINDAGI
# foods = list()
# while True:
#     food = input("Food Name: ")
#     if food == "quit":
#         break
#     foods.append(food)

# print(foods)


##MENTHOS ZINDAGI
foods = list()
while (food :=input("Food Name: "))!= "quit":
    foods.append(food)
print(foods)





sample_data = [
    {"userId": 1,  "name": "rahul", "completed": False},
    {"userId": 1, "name": "rohit", "completed": False},
    {"userId": 1,  "name": "ram", "completed": False},
    {"userId": 1,  "name": "ravan", "completed": True}
]
 
print("With Python 3.8 Walrus Operator:") 
for entry in sample_data: 
    if name := entry.get("name"):
        print(f'Found name: "{name}"')
 
print("Without Walrus operator:")
for entry in sample_data:
    name = entry.get("name")
    if name:
        print(f'Found name: "{name}"')