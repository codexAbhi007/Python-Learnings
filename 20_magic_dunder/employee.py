from typing import Any


class Employee:
    def __init__(self,name) -> None:
        self.name = name

    def __len__(self):
        i = 0 
        for c in self.name:
            i +=1 
        return i

    def __str__(self):
        return(f"The name of the Employee is {self.name}")
    
    def __repr__(self):
        return(f"Object: {self.name}")
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Object call!")

#@__repr__ method in Python defines how an object is presented as a string.