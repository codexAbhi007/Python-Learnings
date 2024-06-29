nums = [1,2,3,4,5,6,7,8,9,10]


#@ 1.1
def gen_func(nums):
    for n in nums:
        yield n**2

my_gen = gen_func(nums)
print(my_gen)
for i in my_gen:
    print(i)


#@ 1.2
my_gen2 = (n**2 for n in nums)
print(my_gen2)
for i in my_gen2:
    print(i)