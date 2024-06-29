class Employee:
    def __init__(self,first,last) -> None:
        self.first = first
        self.last = last
        self.email = f"{self.first}.{self.last}@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"
    

emp1 = Employee('jon','smith')

print(emp1.first)
print(emp1.email)
emp1.first = 'john'
print(emp1.first)
print(emp1.email)
