def myfunc():
    def func2():
        print("HELLO WORLD")
    return func2
myfunc()()

print(myfunc)  ##Returns a function object
#!() represents calling the func not the function full

