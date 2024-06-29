# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i**2)
#     return result 

# my_nums = square_numbers([1,2,3,4,5])

# my_nums = [x*x for x in [1,2,3,4,5]]

# print(my_nums)

def square_numbers(nums):
    
    for i in nums:
        yield(i**2)
        

my_nums = square_numbers([1,2,3,4,5])
for i in my_nums:
    print(i)
