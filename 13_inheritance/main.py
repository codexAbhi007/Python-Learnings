class Employee:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id

    @property
    def showDetails(self):
        print(f"The name of Employee of id {self.id} is {self.name}")


class Programmer(Employee):
    def showLang(self):
        print("The deafult language is Python")


class Farmer(Programmer):
    def showFlower(self):
        print("Hey this is a flower!")



e1 = Employee("Abhirup",101)
e1.showDetails
# e1.showLang() ##ERROR

e2 = Programmer("Harry",420)
e2.showDetails
e2.showLang()

e3 = Farmer("Subham",999)
e3.showDetails
e3.showLang()
e3.showFlower()