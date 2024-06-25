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

#instead of printing the message we can pass a fx as an aurgument to the decorated func
def decorater_func(original_function):
    def wrapper_func():
        print(f"Wrapper executed this before {original_function.__name__}")

        original_function()

        print(f"Wrapper executed this after {original_function.__name__}")

      
    return wrapper_func

#@ example 1 without decorator
def display():
    print("Display Func!")

decorated_display = decorater_func(display)
decorated_display()

## Real decorater!
@decorater_func
def display():
    print("Display Func!")

# decorated_display = decorater_func(display)
# decorated_display()

display()

