class vector:
    def __init__(self,i,j,k) -> None:
        self.i = i
        self.j = j
        self.k = k

    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(x,y):
        return vector(x.i + y.i, x.j + y.j,  x.k+y.k)
    
    def __mul__(x,y):
        return f"{x.i - y.i}i + {x.j - y.j}j + {x.k - y.k}k"

v1 = vector(1,2,3)
v2 = vector(5,1,3)
print(v1)
print(v2)
print(v1+v2)
print(type(v1+v2))
print(v1-v2)
print(type(v1-v2))