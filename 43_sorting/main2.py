class Employee:
    def __init__(self,name,age,salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self) -> str:
        return f"Employee({self.name!r},{self.age!r},{self.salary!r})"
    

e1 = Employee('Carl',40,50000)
e2 = Employee('Magnus',56,20000)
e3 = Employee('Root',30,80000)

employees = [e1,e2,e3]

def e_sort_salary(emp):
    return emp.salary
# def e_sort_age(emp):
#    return emp.age
def e_sort_name(emp):
    return emp.name

s_employees1 = sorted(employees,key = e_sort_salary,reverse=True)
s_employees2 = sorted(employees,key = e_sort_name)
s_employees3 = sorted(employees,key = lambda e: e.age) 

print(s_employees1,'\n',s_employees2,'\n',s_employees3)
