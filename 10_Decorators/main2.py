def my_decorater(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

def my_func():
    print("HELLO WORLD")

hello_world = my_decorater(my_func)
hello_world()


##THE ABOVE CAN BE WRITTEN AS --> 


def my_decorater(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@my_decorater
def my_func():
    print("HELLO WORLD")

my_func()
