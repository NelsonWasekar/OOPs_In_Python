

# Hybrid Inheritance (Diamond Problem)
'''
class A:
      def m1(self):
         print("m1---A")

class B(A):
    def m1(self):
        print("m1---B")
        super().m1()
        #A.m1(self)
class C(A):
    def m1(self):
        print("m1---C")
        # super().m1()

class D(B, C):
      pass

d=D()
d.m1()
print(D.__mro__)
'''

#################################################################################################

'''
# Multilevel Inheritance

class A:
    def m1(self):
        print("M1--A")

    def m2(self):
        print("M2--A")

class B(A):
    def m1(self):
        print("M1--B")

    def m3(self):
        print("M3--B")

class C(B):
     pass

# class C(B):
#     def m1(self):
#         print("M1__C")

c=C()
# c.m1()
c.m2()
# c.m3()
print(C.mro())

'''
################################################################################################3

'''
# Multiple Inheritance

class A:
    def m1(self):
        print("M1--A")

    def m2(self):
        print("M2--A")

class B:
    def m1(self):
        print("M1--B")

    def m3(self):
        print("M3--B")


# class C(A,B):
#     pass

class C(B,A):
     pass

c=C()
c.m1()
print(C.mro())
# print(issubclass(C, B))
# print(isinstance(c))
'''
#########################################################################
'''

# Hierarchy Inheritance

class A:
    def m1(self):
        print("M1--A")

    def m2(self):
        print("M2--A")

class B(A):
   pass

class C(A):
    pass

c=C()
c.m9()
'''
########################################################################3

# Dimaond Or Hybrid Inheritance
'''
class A:
    x = 5
    a = 10
    b = 20
    def m1(self):
        print("M1--A")

    def m2(self):
        print("M2--A")

class B(A):
    c = 30
    b = 200
    def m3(self):
        print("M3--B")

    def m2(self):
        print("M2--B")

class C(A):
    x = 500
    d = 40
    b = 200
    def m1(self):
        print("M1--C")

    def m2(self):
        print("M2--C")

class D(B,C):
    e = 50
    b = 20000
    def m5(self):
        print("M5--D")

    def m2(self):
        print("M2--D")


d=D()
# print(d.e)
# print(d.b)
# d.m5()
# d.m2()
print(d.x)
# d.m1()

c=C()
# print(c.e)
# print(c.b)
# c.m5()
# c.m2()
# print(c.x)


b=B()
# print(b.a)
# print(b.b)
#b.m5()
# b.m2()
#print(b.e)
'''

################################################################################################
'''
# Multiple Inheritance

class A:
    def m1(self):
        print('M1--A')
class B:
    def m2(self):
        print('M2--A')

class C(B,A):
    def m3(self):
        print('M3--C')


c=C()
c.m1()
print(C.mro())
'''
##################################################################

'''
# single Inheritance

class A:
    def m1(self):
        print("M1--A")
class B(A):
    def m2(self):
        print("M2--B")

b=B()
b.m2()
print(B.mro())
'''

######################################################################################
