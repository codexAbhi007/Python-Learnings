class Person:
    name = "Abhi"
    occupation = "Programmer"
    networth = 15000
    def info(self):
        print(f"Name - {self.name}\nOccupation - {self.occupation}\nNetworth - {self.networth}")


a = Person()
a.name = "a"
a.occupation = "gardner"
a.networth = 1000
a.info()

##self is refering to that particular object for which the function is called

c = Person()
c.info()