class Dog:
    kind = "Bulldog"
    def __init__ (self, name, age=0):
        self.name = name
        self.age = age
a = Dog("Baduk", 2)
b = Dog("Marry", 3)

print(a.kind)
print(b.kind)
print(Dog.kind)

print(a.name)
print(b.name)
