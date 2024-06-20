from employee import Employee
#@ https://www.geeksforgeeks.org/dunder-magic-methods-python/

e = Employee("Abhi")
print(e) ##this is will call the __str__ method other wise it will show something <employee.Employee object at 0x000001481CF95B50>
##if str is not present it call the __repr__ method 
print(str(e)) ##still calls repr

print(repr(e))

e()