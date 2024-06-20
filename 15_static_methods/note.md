
# What is a static method?

Static methods in Python are extremely similar to python class level methods, the difference being that a static method is bound to a class rather than the objects for that class. This means that a static method can be called without an object for that class. This also means that static methods cannot modify the state of an object as they are not bound to it. Let’s see how we can create static methods in Python.


# Creating python static methods
Python Static methods can be created in two ways. Let’s see each of the ways here:

Using `staticmethod()`
Let’s directly jump to sample code snippet on how to use the staticmethod() approach:
```python
class Calculator:

    def addNumbers(x, y):
        return x + y

#create addNumbers static method
Calculator.addNumbers = staticmethod(Calculator.addNumbers)

print('Product:', Calculator.addNumbers(15, 110))
```
Note that we called the addNumbers we created without an object.
There were no surprises there. This approach is controlled as at each place, it is possible to create a static method out of a class method as well. Let’s see another approach with the same example here.
# Using @staticmethod
This is a more subtle way of creating a Static method as we do not have to rely on a statement definition of a method being a class method and making it static at each place you make it static. Let’s use this annotation in a code snippet:
```python
class Calculator:

    # create addNumbers static method
    @staticmethod
    def addNumbers(x, y):
        return x + y

print('Product:', Calculator.addNumbers(15, 110))
```
This was actually a much better way to create a static method as the intention of keeping the method static is clear as soon as we create it and mark it with the `@staticmethod` annotation.