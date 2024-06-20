## Returning the Inner Function
Instead of calling the inner function inside the outer function, you can return the inner function itself. This is where it gets interesting and useful for decorators.

```bash
def outer_function():
    def inner_function():
        print("Hello from the inner function!")
    return inner_function

# Assign the returned function to a variable
my_function = outer_function()

# Call the returned function
my_function()
```
1. outer_function is defined.
2. Inside outer_function, another function called inner_function is defined.
3. outer_function returns the inner_function.
4. When you call outer_function, it returns inner_function.
5. The returned function (which is inner_function) is assigned to my_function.
6. When you call my_function(), it calls inner_function, resulting in the output "Hello from the inner function!".

## Why Return the Inner Function?
Returning the inner function is useful because it allows you to create flexible and reusable pieces of code. This concept is heavily used in decorators to modify the behavior of functions.

## Without Decorator
```bash
def simple_decorator(func):
    def inner_function():
        print("Before calling the function")
        func()
        print("After calling the function")
    return inner_function

def say_hello():
    print("Hello!")

# Apply the decorator
decorated_function = simple_decorator(say_hello)

# Call the decorated function
decorated_function()
```


## Applying Decorators Using @ Syntax
```bash
@simple_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
```
In this case, @simple_decorator is syntactic sugar for:
```bash
def say_hello():
    print("Hello!")

say_hello = simple_decorator(say_hello)
```