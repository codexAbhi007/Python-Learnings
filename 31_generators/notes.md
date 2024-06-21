# Generators
A Generator in Python is a function that returns an iterator using the Yield keyword.

A generator function in Python is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a Python generator function. 

Python Generator functions return a generator object that is iterable, i.e., can be used as an Iterator. Generator objects are used either by calling the next method of the generator object or using the generator object in a “for in” loop.

```python
# A Python program to demonstrate use of  
# generator object with next()  
  
# A generator function 
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
   
# x is a generator object 
x = simpleGeneratorFun() 
  
# Iterating over the generator object using next 
  
# In Python 3, __next__() 
print(next(x)) 
print(next(x)) 
print(next(x))
```

```python
# A simple generator for Fibonacci Numbers 
def fib(limit): 
	
	# Initialize first two Fibonacci Numbers 
	a, b = 0, 1

	# One by one yield next Fibonacci Number 
	while a < limit: 
		yield a 
		a, b = b, a + b 

# Create a generator object 
x = fib(5) 

# Iterating over the generator object using next 
# In Python 3, __next__() 
print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 

# Iterating over the generator object using for 
# in loop. 
print("\nUsing for in loop") 
for i in fib(5): 
	print(i)
```

## Python Generator Expression
In Python, generator expression is another way of writing the generator function. It uses the Python list comprehension technique but instead of storing the elements in a list in memory, it creates generator objects.

Generator Expression Syntax
The generator expression in Python has the following Syntax:

`(expression for item in iterable)`

```py
# generator expression 
generator_exp = (i * 5 for i in range(5) if i%2==0) 

for i in generator_exp: 
	print(i)

```

## What does the Yield Keyword do?
yield keyword is used to create a generator function. A type of function that is memory efficient and can be used like an iterator object.

## Difference between return and yield Python
The yield keyword in Python is similar to a return statement used for returning values in Python which returns a generator object to the one who calls the function which contains yield, instead of simply returning a value. The main difference between them is, the return statement terminates the execution of the function. Whereas, the yield statement only pauses the execution of the function. Another difference is return statements are never executed. whereas, yield statements are executed when the function resumes its execution.

### Advantages of yield:

Using yield keyword is highly memory efficient, since the execution happens only when the caller iterates over the object.
As the variables states are saved, we can pause and resume from the same point, thus saving time.
### Disadvantages of yield: 

Sometimes it becomes hard to understand the flow of code due to multiple times of value return from the function generator.
Calling of generator functions must be handled properly, else might cause errors in program.

```py
# generator to print even numbers
def print_even(test_list):
	for i in test_list:
		if i % 2 == 0:
			yield i

# initializing list
test_list = [1, 4, 5, 6, 7]

# printing initial list
print("The original list is : " + str(test_list))

# printing even numbers
print("The even numbers in list are : ", end=" ")
for j in print_even(test_list):
	print(j, end=" ")
```

