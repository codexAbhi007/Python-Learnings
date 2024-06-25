def outer_func(msg):
    

    def inner_func():
        print(msg)
      
    return inner_func

hi_func = outer_func('Hi')
bye_func = outer_func('Bye')

hi_func()
bye_func()

#A decorator is just a function that takes another function as an argument, adds some kind of functionality, and then returns another function without altering the source code of the original func

def decorater_func(msg):
    def wrapper_func():
        print(msg)
      
    return wrapper_func

#instead of printing the message we can 