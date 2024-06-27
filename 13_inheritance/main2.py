class Employee:

    raise_amt = 1.04

    def __init__(self,first,last,pay) -> None:
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay  * self.raise_amt)


class Developer(Employee):

    def __init__(self, first, last, pay,prog_lang) -> None:
        super().__init__(first, last, pay) #or
        # Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay,employees=None) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            print("Added",emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print("Removed",emp)

    def display_employees(self):
        print("Employees: ",end='')
        for i in self.employees:
            
            print(i.fullname(),sep =",")




dev_1 = Developer("Abhi","G",50000,'python')
dev_2 = Developer("Tom","Test",3000,'java')

print(dev_1.email)
print(Developer.mro())
# print(help(Developer))
# print(dev_1.__dict__)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1 = Manager("Sue","Smith",90000,[dev_1,dev_2])

print(mgr_1.email)

mgr_1.display_employees()

print(dev_1.raise_amt)
dev_1.raise_amt = 2.5
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_2.pay)

print(dev_1.raise_amt)
dev_1.apply_raise()
print(dev_1.pay)


