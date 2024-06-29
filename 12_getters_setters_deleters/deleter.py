class Employee:

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleted!")
        
        self.first = self.last = None
  

emp1 = Employee("Abhirup", "Ghosh")
emp1.first = "Abhi"
emp1.last = "G"

print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)


emp1.fullname = "John Smith"
print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)


## NOW WE WANT TO DELETE THE FULLNAME WE CANNOT DELETE EASILY
#del emp1.fullname #!AttributeError: property 'fullname' of 'Employee' object has no deleter

## SO WE DEFINE A DELETER
del emp1.fullname

print(emp1.first)
print(emp1.last)
print(emp1.fullname)

