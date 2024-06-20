def average(*numbers): ##TAKES ARGUMENTS AS A TUPLE
    print(numbers)
    print(type(numbers))
    s = 0 
    for i in numbers:
        s = s + i
    print("Average is ",s/len(numbers))

average(5,6,4,5,1,2,12,121212)




def name(**name): ##TAKES KEYWORD ARGUMENTs AS DICTIONARY
    print(name)
    print(type(name))
    print(f"HELLO {name["fname"]} {name["mname"]} {name["lname"]}")

name(fname = "abhi" ,lname = "ghosh", mname ="rup")






def order_pizza(size, *toppings, **details):
    print(f"Ordered a {size} pizza with following toppings:")
    print(toppings)
    for topping in toppings:
        print(f" - {topping}")
    print(details)
    for key, value in details.items():
        print(f"{key} - {value}")


order_pizza("large","pepper","paneer","extracheese", delivery = True, tip =20)