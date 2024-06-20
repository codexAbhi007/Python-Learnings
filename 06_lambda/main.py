#Lambda func is like arrow func in js 


def add_traditional(x,y,z):
    return x+y+z

print(add_traditional(5,61,7))

## Using Lambda Function

add = lambda x,y,z:x+y+z
print(add(5,6,7))

avg = lambda x,y: (x+y)/2

print(avg(10,15))


## Function returning a function

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

## FUnction can also be passed inside a function

def apply(fx,value):
   return 5 + fx(value)


result = apply(lambda x: x**2,4)
print(result)