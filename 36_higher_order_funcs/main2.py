#great example is a custom map function
def square(x):
    return x ** 2

def cube(x):
    return x ** 3
def my_map(func, arg_list):
    result = []

    for i in arg_list:
        result.append(func(i))
    return result


my_arr = [1,2,3,4,5,6,7]
squares = my_map(square,my_arr) #parentheses is not required here! as parenthese meaning calling the function then and there
triples = my_map(cube,my_arr)
print(squares)
print(triples)

