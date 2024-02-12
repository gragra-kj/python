class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont know what to say")



class Cat(Pet):
    def __init__(self,name,color,age):
        super().__init__(name,age)
        self.color=color

    def speak(self):
        print("Meow")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and i am {self.color}")


class Dod(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p=Pet("Tim",8)
p.show()
c=Cat("Greg","black",9)
c.show()
c.speak()
d=Dod("Pheebs",2)
d.show()
d.speak()
f=Fish("GG" ,9)
f.speak()
