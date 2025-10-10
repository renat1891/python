class Animal:
    legs = 4
    eyes = 2


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_woof(self):
        print("Woof! My name is", self.name, self.legs)


class Bird(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.legs = 2  # Birds have 2 legs

    def say_chirp(self):
        print("Chirp! My name is", self.name)


dog1 = Dog("Bobik", 3)
dog1.say_woof()
print("I have", dog1.legs, "legs and", dog1.eyes, "eyes.")


bird1 = Bird("Tweety", 1)
bird1.say_chirp()
print("I have", bird1.legs, "legs and", bird1.eyes, "eyes.")