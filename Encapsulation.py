############################################################################################

class A:
    a=10
    __b=20
    _c=30

    def m1(self):
        print(self.__b)
        # pass

class B(A):
     def m2(self):
         print(self.a)
         print(self._c)
         #print(self.__b)       #Private Variable

         #super().m1()

b=B()
b.m2()

#print(b.a)
#print(b._c)
#print(b.__b)

# a1=A()
# a1.m1()

# print(a1._c)
# print(a1.a)
# print(a1.__b)
# print(a1._A__b)

######################################################################################################################

'''
class A:
    a=10
    __b=20
    _c=30

class B(A):
     def m2(self):
         print(self.a)
         print(self._A__b)      #Name Mangling
         print(self._c)

b=B()
#b.m2()

print(b.a)
print(b._c)
print(b._A__b)    # Name Mangling

'''
##########################################################################################################

'''
# Setters and Getters method for private variable

class Student():
       def setRollno(self, rollno):
           self.__rollno=rollno

       def setName(self, name):
            self.__name=name

       def getRollno(self):
           return self.__rollno

       def getName(self):
           return self.__name


s1=Student()
s1.setRollno(1)
s1.setName("XYZ")

print(s1.getRollno())
print(s1.getName())

# s2=Student()
# s2.setRollno(2)
# s2.setName("PQR")
#
# print(s2.getRollno())
# print(s2.getName())
'''
###############################################################################################

'''

# Setter and Getter Methods for Public, Protected, Private


class Student():

    def setRollno(self, rollno):
        self.rollno=rollno

    def setName(self, name):
        self._name=name

    def setMarks(self, marks):
        self.__marks=marks

    def getRollno(self):
        return self.rollno

    def getName(self):
        return self._name

    def getMarks(self):
        return self.__marks

s1=Student()
s1.setRollno(1)
s1.setName("Shivaji")
s1.setMarks(50)

print(s1.getRollno(), end= " ")
print(s1.getName(), end= " ")
print(s1.getMarks())



# s2=Student()
# s2.setRollno(2)
# s2.setName("Akshay")
# s2.setMarks(60)
#
# print(s2.getRollno(), end=" ")
# print(s2.getName(), end=" ")
# print(s2.getMarks())
#
#
# s3=Student()
# s3.setRollno(3)
# s3.setName("Abhijeet")
# s3.setMarks(70)
#
# print(s3.getRollno(), end=" ")
# print(s3.getName(), end=" ")
# print(s3.getMarks())

'''

##########################################################################################################33

'''
# IMP concept for Private variable

class A:
    a=10
    _b=30
    __c=50
    # print()
    # print(__c)

a1=A()
# print(a1.a)
# print(a1._b)
#print(a1.__c)   #Private variable can't be access outside of the class

a1.a=200
print(a1.a)

a1._b=300
print(a1._b)

a1.__c=500
print(a1.__c)
'''



##########################################################################################################################

'''
# Very Important concept of private variable and Checking Its Id

class Student():
    __rn=0
    name=' '
    def showData(self):
        print(self.__rn)
        print(self.name)
        print(id(self.__rn))

s1=Student()
s1.__rn=1
s1.name="XYZ"

s1.showData()

# print(s1.__rn)
# print(s1.name)

# print(id(s1.__rn))

# print(s1._Student__rn)     #Name Mangling

'''
##########################################################################################################################
'''

# Very Important concept of protected variable and Checking Its Id

class College:
       __a=10
       _b=10
       c=1

       def display(self):
           # print(self.__a)
           print(self._b)
           print(id(self._b))
           # print(id(self.c))

c1=College()
c1.__a=50

# print(c1.__a)
c1._b=500


# print(c1._b)
print(id(c1._b))            # why protected variable giving same id.....????

c1.display()


# print(c1._b)
# print(dir(College))

# c1.c=899
# print(id(c1.c))
'''
##############################################################################################

'''
# Only variable declaration in class and its access exposure

class B:
     a=10
     _b=20
     __c=30

b=B()

b.a=401

print(b.a)
# print(id(b.a))

b._b=685
print(b._b)

b.__c=108
print(b.__c)

'''
###############################################################################################
'''
class A:
      __c=500
      def display(self,c):
          self.__c=c
      # def setValue

a=A()
print(a.display(1))
'''
#####################################################################################################