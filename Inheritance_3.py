# Combination of 2 types of Inheritance

class Grandfather():
     def __init__(self, n, a):
         self.name= n
         self.age=a
     def __str__(self):
          return f" Your Name : {self.name}, Your Age : {self.age}"

class Father(Grandfather):
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def __str__(self):
        return f"Name : {self.name}, Age : {self.age}"

    def display(self):
            print("I m a Father")

class Son(Father):
      def display(self):
          print("I m a son")

class Daughter(Father):
      def display(self):
          print("I am a Daughter")


f1=Father("Shivaji", "85")
#print(f1)
# f1.display()

s1=Son("Shivam", "40")
# print(s1)
# s1.display()

d1=Daughter("Akshay", "39")
# print((d1))
# d1.display()

######################################################################################################################