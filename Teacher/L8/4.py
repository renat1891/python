class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_woof(self):
        print("Woof! My name is", self.name)

dog1 = Dog("Bobik", 3)
dog1.say_woof()

dog2 = Dog("Sharik", 5)
dog2.say_woof()