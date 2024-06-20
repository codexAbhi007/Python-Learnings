#@ https://www.digitalocean.com/community/tutorials/python-static-method


def add(a,b): ##THIS WORKS DIFFERENT
    return a-b


class Math():
    def __init__(self,num) -> None:
        self.num = num
    
    def addtonum(self,n):
        self.num = self.num + n
    
    @staticmethod
    def add(a,b): ##THIS WORKS DIFFERENT
        return a+b
    

print(Math.add(7,2)) ##CAN BE CALLED WITHOUT MAKING AN OBJECT OR INSTANCE OF THE CLASS
a = Math(5) 
print(a.add(5,2)) ## CAN BE CALLED WITH AN INSTANCE ALSO
print(add(7,2))

#! self is not necessary in a static method