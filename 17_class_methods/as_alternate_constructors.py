class Employee:
    def __init__(self,name, salary) -> None:
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

e1 = Employee("Harry",12000)
print(e1.name,e1.salary)

##SUPPOSE SOMEONE GAVE DATA AS this
data = "Abhi-15000" ##and told to parse this data and make an instance of Employee

e2 = Employee(data.split("-")[0],data.split("-")[1])
print(e2.name,e2.salary)

##here is a problem we have to write it eveyrtime split. this will make our code ugly
#if we change our init the previous method wont work then so to handle this we use @classmethod as alternative consructors

data2 = "Adi-20000"
e3 = Employee.fromStr(data2)
print(e3.name,e3.salary)


class Rectangle:
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height

    @classmethod
    def square(cls,size): ##cls refering to Rectangle class 
        return cls(size,size) ##CREATING AN INSTANCE === Rectangle(size,size)
    

sq = Rectangle.square(10)
print(sq.width)
print(sq.height)