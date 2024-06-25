# A closure in Python is a function object that remembers values in enclosing scopes even if they are not present in memory. Closures are created when a nested function references a value in its enclosing scope. The closure captures these values and keeps them alive so that they can be used when the nested function is called, even if the outer function has finished execution.

def outer_func():
    msg = 'Hi'

    def inner_func():
        print(msg) #msg is called the free variable because its not actually defined in the inner function but we still have access to inner function 

    return inner_func



my_func = outer_func() #now my_func is actually = 

print(my_func.__name__)
my_func()
my_func()
my_func()
my_func()
#nwo this is interesting as we have completed our execution of outer_func but when we re running my_func its actually running the inner function which has still access to the msg variable -- this is what a closure

#so closure is an inner func that remembers and has access to the local scope in which it was created even after the outer func is getting executed

def outer_func2(msg):
    message = msg

    def inner_func2():
        print(message) #msg is called the free variable because its not actually defined in the inner function but we still have access to inner function 

    return inner_func2

hi_func = outer_func2('HI')
hello_func = outer_func2('HELLO')
hi_func()

hello_func()

#each of this func remembers its values of its own message variable 
#! a closure closes over the free variables from their environment 