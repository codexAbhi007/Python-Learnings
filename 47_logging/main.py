import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected. ddefault method 

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename=r'47_logging\test.log', level=logging.DEBUG)
logging.basicConfig(filename=r'47_logging\test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x * y

def div(x,y):
    return x/y

num1 = 30
num2 = 10

add_result = add(num1,num2)
# print(f"Add: {num1} + {num2} = {add_result}")
# logging.debug(f"Add: {num1} + {num2} = {add_result}")
# logging.warning(f"Add: {num1} + {num2} = {add_result}")
logging.debug(f"Add: {num1} + {num2} = {add_result}")

sub_result = sub(num1,num2)
# print(f"Add: {num1} - {num2} = {sub_result}")
# logging.debug(f"Add: {num1} - {num2} = {sub_result}")
# logging.warning(f"Add: {num1} - {num2} = {sub_result}")
logging.debug(f"Substract: {num1} - {num2} = {sub_result}")

mul_result = mul(num1,num2)
# print(f"Add: {num1} * {num2} = {mul_result}")
# logging.debug(f"Add: {num1} * {num2} = {mul_result}")
# logging.warning(f"Add: {num1} * {num2} = {mul_result}")
logging.debug(f"Multiply: {num1} * {num2} = {mul_result}")

div_result = div(num1,num2)
# print(f"Add: {num1} / {num2} = {div_result}")
# logging.debug(f"Add: {num1} / {num2} = {div_result}")
# logging.warning(f"Add: {num1} / {num2} = {div_result}")
logging.debug(f"Divide: {num1} / {num2} = {div_result}")

print('DONE!')