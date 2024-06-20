x = [1,2,3,4]
print(dir(x))

##The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. it is a useful tool for discovering what you can do with an object.

class Employee:
    
    company = "Apple"

    def show(self):
        '''Method is used to display data'''
        print(f"The name is {self.name} and company is {self.company}")
    
    def changeCompany(instance,newCompany):
        instance.company = newCompany

    @classmethod
    def changeClassCompany(cls,newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Harry"

e1.show()
print(e1.__dict__) 
##__dict__ attribute returns a dictionary representation of an oject's attributes. 

print(help(Employee))