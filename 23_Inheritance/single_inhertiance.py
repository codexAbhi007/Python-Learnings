class Animal:
    def __init__(self,name,species) -> None:
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by Animal")

class Dog(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name, species="Dog")

        self.breed = breed

    def make_sound(self):
        print("Bark!")


d1 = Dog("Pop","Pitbull")

d1.make_sound()

a = Animal("Yo","Bird")
a.make_sound()
