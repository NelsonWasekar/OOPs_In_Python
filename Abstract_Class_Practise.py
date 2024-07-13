
from abc import ABC, abstractmethod
'''class A(ABC):

      @abstractmethod
      def m1(self):
          #print("M1---A")
          pass

      def m4(self):
          print("M4---A")
          #pass

class B(A):
     def m1(self):
         print("M1---B")
         super().m1()
         print("Nelson")

a1=B()
a1.m1()'''
########################################3###########################
# Multilevel Inheritance

'''
class A(ABC):
    @abstractmethod
    def m1(self):
        print("m1---A")

    @abstractmethod
    def m2(self):
        print("m2---A")

class B(A):
    def m1(self):
       pass
       super().m2()

    # def m2(self):
    #    pass

class C(B):
    def m2(self):
        pass
        A.m1(self)


c1=C()
c1.m1()
# b1=B()
# b1.m1()
print(C.mro())
'''
#####################################################################################
# Hierarchy

'''
class A(ABC):

    @abstractmethod
    def m1(self):
        pass
    
    @abstractmethod
    def m4(self):
        pass
    
class B(A):
   def m1(self):
     print("M1---B")

   def m4(self):
       print("M4---B")

class C(A):
    def m1(self):
        print("M1---C")
    # def m4(self):
    #     print("M4---C")

# c=C()
# c.m4()

b=B()
b.m4()
print(C.mro())
'''
############################################################################################
# Mutlipal Inheritance

'''
class A(ABC):
     # @abstractmethod
     # def m1(self):
         pass

class B():
     # @abstractmethod
     # def m1(self):
     #   print("M1--B")
       pass

class C(A, B):
     def m1(self):
        print("M1----C")
        #super().m1()

c=C()
c.m1()
print(C.mro())  '''
##################################################################################################

# Hybrid Inheritance
'''
class A(ABC):
    
     @abstractmethod
     def m1(self):
        print("M1---A")

class B(A):
    # @abstractmethod
    # def m1(self):
    #     print("M1---B")
    #
    def m1(self):
        print("M1---B")
    # pass

class C(A):
    # @abstractmethod
    # def m1(self):
    #     print("M1---C")

    # def m1(self):
    #    print("M1---C")
    pass

class D(B,C):

    def m4(self):
        print("M1---D")
d1=D()
d1.m1()

# c1=C()
# c1.m1()
# b1=B()
# b1.m1()

print(D.mro())
'''
###################################################################################


class College:
      n="MIT"

      @classmethod
      def display(cls, a,b):
          print(cls.n)
          #print((College.n))
          print(a)
          print(b)

College.display(5,4)
# print(cls.a)
# print(cls.b)

# c1=College()
# c1.display(5,4)
####################################################################3
'''class A:
     @staticmethod
     def dis(a,b):
         print("Nelson")

A.dis(5,2)'''
#################################################################################################