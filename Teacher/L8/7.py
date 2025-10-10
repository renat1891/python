class Num():
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
    
    def __str__(self):
        return str(self.value)
    

n1 = Num(77)
n2 = Num(33)

n3 = n1 + n2
print(n3) 
