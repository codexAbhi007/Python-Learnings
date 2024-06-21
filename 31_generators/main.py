# we will create a simple generator that will yield three integers. Then we will print these integers by using Python for loop.


def simpleGenerator(): 
    yield 1            
    yield 2            
    yield 3            
   

for value in simpleGenerator():  
    print(value)

r = simpleGenerator()
print(r) ##Returns a generator object