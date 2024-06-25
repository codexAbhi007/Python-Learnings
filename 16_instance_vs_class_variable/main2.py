class Employee:
    company = "Google"
    raise_amount = 0.05
    no_of_employee = 0

    def __init__(self,name) -> None:
        self.name = name
        Employee.no_of_employee += 1

    def show_name(self):
        print(f"Name: {self.name}")

    def show_company_strength():
        print(Employee.no_of_employee)

emp1 = Employee("Abhi")
print(emp1.__dict__)
print(emp1.raise_amount)

emp1.raise_amount = 0.06
print(emp1.raise_amount)
print(Employee.raise_amount)
print(emp1.__dict__)