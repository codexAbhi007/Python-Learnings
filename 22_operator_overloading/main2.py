class MyClass:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

obj = MyClass()
print(obj.add(2, 3)) 