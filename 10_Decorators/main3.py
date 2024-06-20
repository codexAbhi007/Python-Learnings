def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorated!")
        
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

## THE ABOVE IS SAME AS 

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorated")
        return func(*args, **kwargs)
    return wrapper

def greet(name):
    print(f"Hello, {name}!")

# Manually apply the combined decorator
greet = my_decorator(greet)

# Call the decorated function
greet("Alice")