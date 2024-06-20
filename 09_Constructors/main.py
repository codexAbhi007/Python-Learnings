# class Person:
#     name = "Abhi"
#     occ = "Developer"

#     def info(self):
#         print(f"{self.name} is {self.occ}")



# a = Person()
# a.name = "Subham"
# a.occ = "Farmer"
# a.info()

##Now problem is we dont want to initialize name and occ as dummy values we want the class to automatically set the name and occ whenever an object is made thts why we use __init__

class Person:
    def __init__(self,name,occ) -> None:
        # print("Hey a class is created!")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is {self.occ}")

## so this is a constructor so whenever we create an object of this class the constructor method is called automatically 

a = Person("Subham","farmer") #@PRINTS 

a.info()

##when the constructor doesnt accept any arguments from the object and has only one argumne (self) then this constructor is called default constructor and when it takes arguments it is called paraametreized constructor 