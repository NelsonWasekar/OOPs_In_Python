class Animal:
     def __init__(self, t,b, c):
          self.types=t
          self.breed=b
          self.color=c

     def __str__(self):
         return f"Type = {self.types}, Breed = {self.breed}, Color = {self.color}"

     def can_swim(self):
        print("It can Swim")

     def can_fly(self):
        print("It can Fly")

     def can_walk(self):
        print("It can Walk")

class Parot(Animal):
       def can_swim(self):
           print("It can not swim")
           super().can_fly()
           super().can_walk()

class Cat(Animal):
    def can_swim(self):
        print("It can not Swim")
    def can_fly(self):
         print("It can not fly")
         super().can_walk()

class Fish(Animal):
    def can_fly(self):
        print("It can not fly")
        print("It can not walk")
        super().can_swim()


class Dog(Animal):

    def can_fly(self):
        print("It can not fly")
        super().can_walk()
        super().can_swim()

p1=Parot("Omnivirous", "NA", "Green")
# print(p1)
# p1.can_swim()


c1=Cat("American", "NA", "White")
# print(c1)
# c1.can_swim()
# c1.can_fly()

f1=Fish("South_African", "Shark", "Black")
# print(f1)
# f1.can_fly()

d1=Dog("Indian", "NA", "Red")
print(d1)
d1.can_fly()
