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



emp1 = Employee("Abhirup", "Ghosh")
emp1.first = "Abhi"
emp1.last = "G"

print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)


## NOW WE WANT TO CHANGE THE FULL NAME AND IT SHOULD AUTOMATICALLY BE DISPLAYED ON FIRST LAST AND EMAIL ACCORDINLY WE CANT SET A ATTRIBUTE DIRECTLY

#emp1.fullname = "John Smith"  #!AttributeError: property 'fullname' of 'Employee' object has no setter

##SO WE DEFINE A SETTER
emp1.fullname = "John Smith"
print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)

