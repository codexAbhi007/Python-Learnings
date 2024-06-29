import logging

logging.basicConfig(filename= '47_logging/employee.log', level= logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')



class Employee:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        # print(f'Created Employee: {self.name} - {self.age} years old - {self.email}')
        logging.info(f'Created Employee: {self.name} - {self.age} years old - {self.email}')
        
    @property
    def email(self):
        return f'{self.name}@gmail.com'
    
    
emp1 = Employee('John',20)
emp2 =Employee('Abhi',18)