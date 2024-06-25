#In Python, functions are first-class citizens. This means that functions in Python can be treated like any other object. They can be created at runtime, passed as arguments to other functions, returned from functions, and assigned to variables. This capability is a fundamental aspect of Python's flexibility and supports a functional programming style within the language.

def square(x):
    return x**2

f = square(5)

print(square)
print(f)

##MENTHOS ZINDAGI

g = square #parentheses only means we re executing or calling a function
print(g)
print(g(6)) 

#so a function can be assigned to a variable 