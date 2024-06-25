#Currying is a functional programming concept where a function that takes multiple arguments is transformed into a series of functions, each taking a single argument. This technique is named after the mathematician Haskell Curry.

#In Python, currying can be achieved using nested functions or by leveraging function tools like functools.partial

#When you curry a function, you break down a function that takes multiple arguments into a series of functions that each take a single argument. For example, instead of having a function f(a, b, c), you can have f(a)(b)(c).



def multiply_setup(amount):
    def multiply(number):
        return amount * number
    
    return multiply

doubler = multiply_setup(2) #sets up a doubler function returns the func multiply therefore doubler itself becomes a function which doubles the number passed

tripler = multiply_setup(3) # sets up a tripler function returns the func multiply therefore tripler itself becomes a function which triples the number passed 


#this is the concept of currying 
print(tripler(3))
print(doubler(4))


def add(x):
    def inner1(y):
        def inner2(z):
            return x + y + z
        return inner2
    return inner1

add_curried = add(1)(2)(3)
print(add_curried)


from functools import partial

def multiply(x, y):
    return x * y

multiply_by_2 = partial(multiply, 7)
result = multiply_by_2(7)  # result is 6
print(result)

#In this example:

#partial is used to create a new function multiply_by_2 where the first argument x is fixed to 2.
#When multiply_by_2 is called with 3, it multiplies 2 and 3.