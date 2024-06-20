class Employee:
      def __init__(self,name,id) -> None:
            self.name = name
            self.id = id

class Programmer(Employee):
    #   def __init__(self,name,id,lang):
    #         self.name = name
    #         self.id = id
    #         self.lang = lang

    def __init__(self, name, id,lang) -> None:
         super().__init__(name, id) ##THIS WILL TAKE THE CONSTRUCTOR FROM THE PARENT NO NEED TO DEFINE AGAIN AS DONE ABOVE AND COMMENTED
         self.lang = lang


rohan = Employee("Rohan",420)
harry = Programmer("Harry",1001,"Python")
print(harry.name,harry.id,harry.lang)
