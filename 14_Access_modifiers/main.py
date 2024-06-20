#TYPES OF ACCESS SPECIFIERS
#1. PUBLIC access modifier
#2. PRIVATE access modifier
#3. PROTECTED access modifier
#@ https://www.geeksforgeeks.org/access-modifiers-in-python-public-private-and-protected/

class Employee():
    def __init__(self) -> None:
        self.name = "Abhi"
        self.__id = 101
    
    def __showdetails(self):
        print(f"Name is {self.name}")
        print(f"{self.__id}")

a = Employee()
print(a.name) ##PUBLIC BY DEFAULT
# print(a.__id) ##PRIVATE 
print(a._Employee__id)  ## can be accessess indirectly
a._Employee__showdetails()
# print(dir(a))
print(a.__dir__())

##PRIVATE ATTRIBUTES AND VARIABLES CAN BE ACCESSED DIRECTLY INSIDE THE CLASS AND INDIRECTLY BY NAME MANGLING OUTSIDE OF CLASS. CERTAINLY THERE IS NO SUCH PRVIATE VARIABLES OR ATTRIBUTES IN PYTHOn