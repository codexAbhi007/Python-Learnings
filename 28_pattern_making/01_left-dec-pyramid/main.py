n = int(input("Enter number: "))
c = n 

for i in range(n):
    for j in range(c):
        print("*",end="")
    c = c - 1  
    print()
