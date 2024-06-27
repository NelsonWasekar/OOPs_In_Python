
#######################################################################################################################

from abc import ABC, abstractmethod

'''
class A(ABC):

    @abstractmethod
    def m1(self):
        pass
    
    def m2(self):
        pass

a=A()

'''

############################################################################################################################

'''
class A:
     def m1(self):
         pass

     def m2(self):
         pass

a=A()
'''

##############################################################################################################################

'''
class A(ABC):

     @abstractmethod
     def m1(self):
         pass

     def m2(self):
        print("M2---A")

class B(A):
      def m1(self):
          print("M1---B")
          
b=B()
b.m2()
'''


#######################################################################################################################


'''
class A(ABC):

     @abstractmethod
     def m1(self):
         pass

     @abstractmethod
     def m3(self):
         pass

     def m2(self):
         print("M2----")

class B(A):

    def m1(self):
        print("M1----B")

    def m3(self):
        print("M3---B")

b=B()
b.m2()
'''

#############################################################################################################


'''
class A(ABC):
    @abstractmethod
    def m1(self):
        print("M1-----")

    @abstractmethod
    def m3(self):
        pass

    def m2(self):
        print("M2---")

class B(A):
    def m1(self):
        print("M1---B")
        super().m1()
        
    def m3(self):
        print("M3---B")

b=B()
b.m1()
'''

#################################################################################################################


# Register Method

class A(ABC):
     @abstractmethod
     def m1(self):
         print("M1---")

     @abstractmethod
     def m3(self):
         pass

     def m4(self):
         print("M4---A")

class B:
    def m1(self):
        print("M1---")

    def m3(self):
        pass

A.register(B)   # B is a Virtual Sublclass of A 

print(issubclass(B,A))

b=B()
# b.m1()
b.m4()
print(B.mro())

##################################################################################################

########################################################################################################