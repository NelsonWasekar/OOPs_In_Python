######################################################################################################################

from abc import ABC, abstractmethod

'''
# Hierarchy Inheritance        # Error

class A(ABC):

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class B(A):

    def m1(self):
        print("M1---B")

class C(A):

   def m2(self):
      print("M2---B")


# c=C()
# c.m2()
# b=B()
# b.m2()
'''
######################################################################################################

'''

# Mutlilevel Inheritance      # Not Error 

class A(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class B(A):
    def m1(self):
        print("M1---B")

class C(B):

   def m2(self):
      print("M2---C")


# c=C()
# c.m2()

b=B()
b.m1()

'''
#########################################################################################################

'''

# Multipal Inheritance    # Not Error


class A(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class B:
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class C(A, B):
   def m1(self):
      print("M2---C")

   def m2(self):
      print("M2---C")


c=C()
c.m2()


'''
#######################################################################################

'''

# Hybrid OR Dimond Inheritance     # Not Error


class A(ABC):

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass


class B(A):

    def m1(self):
        print("M1---D")


class C(A):

    def m2(self):
       pass


class D(B,C):

    def m3(self):
        pass

    def m4(self):
        pass
d=D()
d.m1()
d.m2()
print(D.mro())
print(D.__mro__)
# b=B()
# b.m1()

# c=C()
# c.m2()
'''
###########################################################################################