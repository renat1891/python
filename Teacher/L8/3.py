class Dog():
    name = ""
    age = 0

    def say_woof(self):
        print("Woof! My name is", self.name)

dog1 = Dog()
dog1.name = "Bobik"
dog1.age = 3
dog1.say_woof()

dog2 = Dog()
dog2.name = "Sharik"
dog2.age = 5
dog2.say_woof()