#@ higher order funcstion = a function that either:
## 1. accepts a function as an argument or 
##2. returns a function 
##3. in python functions are also treated as objects


#@ Example 1
def loud(text):
    return text.upper() + " LOUD!"

def quiet(text):
    return "Woosh... " + text.lower() 


def hello(func): #~Takes a function as an argumeent
    text = func("HELlo")
    print(text)

# hello(loud)
# hello(quiet)


#@ Example 2 
def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))


#@ Example 3 
def logger(msg):

    def log_message():
        print('Log: ',msg)

    return log_message

log_hi = logger('Hi!')
log_hi()