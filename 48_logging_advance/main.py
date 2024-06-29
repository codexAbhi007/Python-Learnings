import logging
import employee

##when we re importing employee its running before hand. in that file the level is set to info as info level is 20 its got executed before coming to this file's DEBUG level so in sample.log nothing is thown so we make our own custom logger

#@ suppose we want to log only our errors and worse in our log file 

logger2 = logging.getLogger(__name__)
logger2.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

file_handler = logging.FileHandler(r'48_logging_advance\sample.log')
stream_handler = logging.StreamHandler()

file_handler.setLevel(logging.ERROR)

logger2.addHandler(file_handler)
logger2.addHandler(stream_handler)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# logging.basicConfig(filename=r'48_logging_advance\sample.log', level=logging.DEBUG, format='%(asctime)s:%(name)s%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x * y

def div(x,y):
    try:
        result = x/y
        return result
    except ZeroDivisionError:
        # logger2.error('Tried to divide by zero!')
        logger2.exception('Tried to divide by zero!')
  

num1 = 30
num2 = 0

add_result = add(num1,num2)

# logging.debug(f"Add: {num1} + {num2} = {add_result}")
# logging.info(f"Add: {num1} + {num2} = {add_result}")
logger2.debug(f"Add: {num1} + {num2} = {add_result}")

sub_result = sub(num1,num2)

# logging.debug(f"Substract: {num1} - {num2} = {sub_result}")
# logging.info(f"Substract: {num1} - {num2} = {sub_result}")
logger2.debug(f"Substract: {num1} - {num2} = {sub_result}")

mul_result = mul(num1,num2)

# logging.debug(f"Multiply: {num1} * {num2} = {mul_result}")
# logging.info(f"Multiply: {num1} * {num2} = {mul_result}")
logger2.debug(f"Multiply: {num1} * {num2} = {mul_result}")

div_result = div(num1,num2)

# logging.debug(f"Divide: {num1} / {num2} = {div_result}")
# logging.info(f"Divide: {num1} / {num2} = {div_result}")
logger2.debug(f"Divide: {num1} / {num2} = {div_result}")

print('DONE!')