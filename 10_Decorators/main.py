def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

## THE ABOVE IS SAME AS

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)
    return wrapper

def greet(name):
    print(f"Hello, {name}!")

# Manually apply decorators
greet = decorator1(decorator2(greet))

# Call the decorated function
greet("Alice")