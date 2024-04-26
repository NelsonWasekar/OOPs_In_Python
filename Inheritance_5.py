############################################################################################


# Hierarchy Inheritance

class Person:
      # def __init__(self, name, age, dob):
      #    self.name=name
      #    self.age=age
      #    self.dob=dob

      def display(self):
          print("Name : Shivaji")
          print("Age : 25 ")
          print("Dob : 1990")

class Student(Person):
     def display(self):
         super().display()
         print("Roll No : 85")
         print("Marks : 90")

class Employee(Person):
    def display(self):
        super().display()
        print("Emp Id : 101")
        print("Salery : 4520230")

e1=Employee()
# e1.display()

s1=Student()
# s1.display()


##################################################################################################
'''
# Hierarchy Inheritance


class Person:
    def __init__(self, name, age, dob):
       self.name=name
       self.age=age
       self.dob=dob

    def display(self):
         print("Shivaji")
         print("50")
         print("26 Feb")

class Student(Person):

    def display(self):
        super().display()
        print("I m Student")
        print("Roll No : 85")
        print("Marks : 90")


class Employee(Person):
    def display(self):
        print("I m employee")
        super().display()
        print("Emp Id : 101")
        print("Salery : 4520230")


e1=Employee("Shivam", 25, 25)
# print(e1)
# e1.display()

'''
###############################################################################


# Hierarchy Inheritance

class Person:
    def __init__(self, name, age, dob):
       self.name=name
       self.age=age
       self.dob=dob

    def display(self):
         print(f" Name : {self.name}, Age : {self.age}, Dob : {self.dob}")


class Student(Person):
    def __init__(self,rollno, marks, name, age, dob):
        self.rollno = rollno
        self.marks = marks
        super().__init__(name, age, dob)

    def display(self):
         print(f" Roll No : {self.rollno}, Marks : {self.marks}, Name : {self.name}, Age : {self.age}, Dob : {self.dob}")

class Employee(Person):
    def __init__(self, emailid, salery, name ,age, dob):
        self.emailid=emailid
        self.salery=salery
        super().__init__(name, age, dob)

    def display(self):
       print(f" Email id : {self.emailid}, Name : {self.name}, Age : {self.age}, Dob : {self.dob}, Salery : {self.salery}")


e1=Employee("abc@gmail.com",58000, "Shivaji", 45, 21.5)
# e1.display()

s1=Student(101, 40.8, "Shivam", 25, 28)
# s1.display()


#######################################################################################################


