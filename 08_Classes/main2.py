class Employee:
    def __init__(self,id,name,position,salary) -> None:
        self.name = name
        self.id = id
        self.position = position
        self.salary = salary

    def show_details(self):
        print(f"""
ID:{self.id}
name:{self.name}
position:{self.position}
salary:{self.salary}
""")

emp1 = Employee(1,"Abhi","MLop","50000")
print(emp1)

print(emp1.__dict__)
print(id(emp1))
emp1.show_details()
Employee.show_details(emp1)