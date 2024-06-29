import logging
# if __name__ == '__main__':

logger1 = logging.getLogger(__name__)
logger1.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(name)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

file_handler = logging.FileHandler('48_logging_advance/employee.log')

file_handler.setFormatter(formatter)

logger1.addHandler(file_handler)



# logging.basicConfig(filename= '48_logging_advance/employee.log', level= logging.INFO,
#                     format='%(levelname)s:%(asctime)s:%(name)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')



class Employee:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        # print(f'Created Employee: {self.name} - {self.age} years old - {self.email}')
        logger1.info(f'Created Employee: {self.name} - {self.age} years old - {self.email}')
        
    @property
    def email(self):
        return f'{self.name}@gmail.com'
    
    
emp1 = Employee('John',20)
emp2 =Employee('Abhi',18)