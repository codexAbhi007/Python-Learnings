class Employee:
    companyName = "Google" ##this is a class variable this is applicable to all instances
    noOfEmployee = 0 
    def __init__(self,name) -> None:
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployee += 1
    def showdetails(self):
        print(f"The name is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")
    def showCompanyStrength():
        print(Employee.noOfEmployee)


emp1 = Employee("Abhi")
#@ Extra Note
#emp1.showdetails() ## is same as
# Employee.showdetails(emp1) #!therefore emp1 is passed as an argument 

emp2 = Employee("Rohit")
emp2.showdetails()
emp2.raise_amount = 0.05 ##THIS IS A INSTANCE VARIABLE BECAUSE IT IS ASSOCIATED TO INDIVIDUAL INSTANCES AND NOT AS A CLASS ITSELF
emp2.showdetails()

emp2.companyName = "Apple"
emp2.showdetails()
emp1.showdetails()
##NOW HERE emp2.companyName is changing the companyName vraibale to "Apple" but it is getting changed only for emp2 not for all the instances. so this works like this --> Python searches first the instance variable if it is present it will overwrite the class variable only for that instance.. and if there is no instance variable associated to a particular instance it will show the class variable value


##WE CAN CHANGE THE CLASS VARIABLE LIKE THIS 
Employee.companyName = "Meta"
emp1.showdetails()
emp2.showdetails() ## IT WILL STILL BE APPLE AS PYTHON LOOKING FOR INSTANCE VARIABLE FIRST

Employee.showCompanyStrength()