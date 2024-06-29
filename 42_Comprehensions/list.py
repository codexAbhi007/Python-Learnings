nums = [1,2,3,4,5,6,7,8,9,10]



#~Our Goal is to make n**2 for each n 

#@ 1.1
my_list1 =[]
for n in nums:
    my_list1.append(n**2)

print(my_list1) 


#@ 1.2 
my_list2 = [n**2 for n in nums]
print(my_list2)


#@ 1.3
my_list3 = map(lambda n: n**2, nums)
print(list(my_list3))


#~ I want n for each n in nums if n is even

#@ 2.1
my_list4 = []
for i in nums:
    if i % 2 ==0:
        my_list4.append(i)
print(my_list4)

#@ 2.2
my_list5 = [n for n in nums if n%2 ==0]
print(my_list5)

#@ 2.3
my_list6 = filter(lambda n: n%2==0,nums)
print(list(my_list6))

#~ I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'

#@ 3.1
my_list7 = []
for letter in 'abcd':
    for num in range(4):
        my_list7.append((letter,num))
print(my_list7)

#@ 3.2
my_list8 = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list8)