class Employee:
    
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    def changeCompany(instance,newCompany):
        instance.company = newCompany

    @classmethod
    def changeClassCompany(cls,newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla") ##THIS IS NOT CHANING THE CLASS VARIABLE company THE changeCompany func takes argument as instance name (it need not be written sa self) THIS WILL ONLY CHANGE THE THE company name at instance level 
e1.show()
print(Employee.company)

##NOW WE CAN CHANGE THE CLASS VARIABLE
##THE @classmethod decorator takes class name as the first argument and not instance name 
Employee.changeClassCompany("Meta")
print(Employee.company)
e1.show() ##STILL LOCAL VARIABLE IS CALLED