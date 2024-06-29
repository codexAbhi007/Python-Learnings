#Python provides the assert statement to check if a given logical expression is true or false.
#Program execution only procees if the expression is true and raises the AssertionError when it is false. 

# num=1
# assert num>=10

# print('HElloworld')

try:
    num = int(input('Enter the number: '))
    assert num%2==0
    print("The number is Even!")
except AssertionError:
    print("Number is not Even!")
