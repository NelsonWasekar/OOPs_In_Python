
####################################################################################################
'''
class A:

    def m1 (self):
        print("M1--A")

    def m2(self):
        print('M2--A')


class B:

    def m1(self):
        print("M1--B")

    def m2(self):
        print('M2--B')


def common(obj):   # it is type system used in dynamic language
    obj.m1()
    obj.m2()

# o=A()
# common(o)

b=B()
common(b)
'''
############################################################################################################

class A:
    def m1(self):
        print("M1--A")
    def m2(self):
       print("M2--A")

class B:
    def m1(self):
        print("M1--B")

    def m3(self):
       print("M2--B")


# def common(obj):
#     obj.m1()
#     obj.m2()
#
# common(A())
# common(B())       #Error


def common(obj):
       if hasattr(obj, "m1"):
           obj.m1()
       if hasattr(obj, 'm2'):
           obj.m2()
       if hasattr(obj, "m3"):
           obj.m3()

# common(A())    #nameless object define

# a=A()    #object define
# common(a)

common(B())

###################################################################################################
