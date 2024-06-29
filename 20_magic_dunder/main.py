from typing import Any


class Employee:
    def __init__(self,first,last,pay) -> None:
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def __repr__(self) -> str:
        return f"Employee({self.first!r},{self.last!r},{self.pay!r})"
    
    def __str__(self) -> str:
        return f"This is a str method"
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
    
    
emp_1 = Employee("Abhi","Ghosh",10000)
emp_2 = Employee("Corey","Schafer",60000)
print(emp_1)
print(str(emp_1))
print(repr(emp_2))