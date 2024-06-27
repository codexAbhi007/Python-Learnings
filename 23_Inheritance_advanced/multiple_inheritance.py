
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")


class DancerEmployee(Employee, Dancer):

    ## ORDER MATTER HERE THE PARENT CLASS WHICH IS MENTIONED FIRST, FROM THERE THE METHOD show() will be called
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name
    # def show(self):
    #     print(f"The name is {self.name} and dance is {self.dance}")

o = DancerEmployee("kathak", "Shivangi")

print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro()) 

##Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes. Especially it plays vital role in the context of multiple inheritance as single method may be found in multiple super classes. 