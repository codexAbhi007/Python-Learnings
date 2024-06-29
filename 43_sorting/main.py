li = [3,1,332,434,12,64,234,12,4]

s_li = sorted(li)
print(s_li)
print(li)

li.sort()
print(li)

tup = (3,1,332,434,12,64,234,12,4)
s_tup = sorted(tup)
print(s_tup)

li = [-1,-2,-4,0,5,4,4,3,2,6]
s_li = sorted(li)
print(s_li)

s_li = sorted(li,key=abs)
'''A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.'''
print(s_li)