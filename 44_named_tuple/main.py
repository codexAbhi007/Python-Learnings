from collections import namedtuple

# color = (255,0,0)
# print(color[0])


Color_tup = namedtuple('color',['red','green','blue'])


color1 = Color_tup(55,155,255)
print(color1[0])
print(color1.red)
white = Color_tup(255,255,255)
print(white)