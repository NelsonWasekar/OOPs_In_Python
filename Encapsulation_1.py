'''
class Student:
      _b=40
      __a=49

      def display(self):
          print(id(self.__a))
          print(self._b)  #40
          print(self.__a)  #49
          #print(id(self._b))

s1=Student()
s1._b=79
#print(id(s1._b))

s1.__a=88
print(id(s1.__a))
s1.display()   #79,49
print(s1._b)   #79
print(s1.__a)   #88
'''
########################################################################3
'''
class A():
    name=" "
    __z=77
    _v=11

    def display(self):
        print(self.__z)    #77
        print(self.name)   #' '
        print(self._v)    #11

a=A()
a.__z=87
a.name="Nelson"
print(a.__z)  # 87
print(a.name)  # Nelson
a.display()  # 77, Nelson, 11
'''
################################################################################################

'''
class A:
      name=" "
      _b=10
      d=8569

      def m1(self):
          print(self.name)
          print(self._b)
          print(id(self._b))
          print(self.d)
          print(id(self.d))

a=A()
a.name="Nelson"

a.d=5654
print(a.d)
print(id(a.d))

a._b=20
print(a._b)
print(id(a._b))
print("---------------------")
a.m1()
'''
#################################################
