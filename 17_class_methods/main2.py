class Employee:

    num_of_employees = 0
    raise_amount = 0.5

    def __init__(self,first,last,pay) -> None:
        self.first = first
        self.last = last
   
        self.pay = pay
        Employee.num_of_employees += 1 

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amt):
        cls.raise_amount = amt

emp1 = Employee("Abhi","Ghosh",50000)

print(Employee.raise_amount)
print(emp1.raise_amount)

Employee.set_raise_amount(0.7)

print(Employee.raise_amount)
print(emp1.raise_amount)

emp1.set_raise_amount(0.8)

print(Employee.raise_amount)
print(emp1.raise_amount)