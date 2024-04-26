

'''
m1()
m1(int i)
m1(string s)


m1()
m1(5)
m1("XYZ")

'''



######################################################################################
'''
def m1():
    print("M1---")

def m1(a,b):
    print("M1--a,b")

def m1(a,b,c):
    print("M1--a,b,c")


# m1()
# m1(5)
m1(5,4,3)'''
#####################################################################################
'''
class A:
    def sum(self,a,b):
        c=a+b
        print(c)
    def sum(self, a,b,c):
       d=a+b+c
       print(d)

a=A()
# a.sum(10, 20)
a.sum(10,20,30)
'''
#################################################################################33

'''
# Default Parameter method

print(1!=0)
print(0!=0)

class A:
     def sum(self, a=0, b=0, c=0):
         if a!=0 and b!=0 and c!=0:
             print(a+b+c)
         elif a!=0 and b!=0:
            print(a+b)
         else:
            print("pls give atleast 2 values")

a=A()
# a.sum()
# a.sum(10,20)
# a.sum(10,10,40)
# a.sum(10,20,40,10)
'''
#########################################################################################################################

'''
# *a method using class   (Method Overloading using args)

class A:
     def sum(self, *a):
         s=0
         for x in a:
             s=s+x
         print("sum :", s)

a=A()
a.sum()
a.sum(10,20)
a.sum(10,20,30)
a.sum(10,20,30,40)
'''
#######################################################################################################################

'''
# *a method without class     (Method Overloading using args)

def sum(*a):
    s = 0
    for x in a:
        s = s + x
    print("sum :", s)

sum(2,6,6)
sum(10,20,30,100)
sum(2,2,2,2)

'''

######################################################################################################################

'''
from multipledispatch import dispatch

@dispatch(int, int)
def sum(a,b):
    print(a+b)

@dispatch(int, int, int)
def sum(a, b,c):
    print(a+b+c)

@dispatch(float, float, float)
def sum(a, b,c):
    print(a+b+c)

sum(5, 4)
sum(5, 4, 20)
sum(6.3, 4.2, 5.2) 
'''

#############################################################################################################################
'''


# Multiplication using default parameter None

class B:
     def mul(self, a=None, b=None, c=None):
         if a!=None and b!=None and c!=None:
             print(a*b*c)
         elif a!=None and b!=None:
             print(a*b)
         else:
           print("Take at least 2 value")

b1=B()
# b1.mul(5)
# b1.mul(2,2)
# b1.mul(5,2,2)
# b1.mul(1,3,2)
# b1.mul()
#b1.mul(4,2,5,6)

'''
##############################################################################################################

'''
from multipledispatch import dispatch

@dispatch(int, int)
def mul(a, b):
     print(a*b)

@dispatch(float, float, float)
def mul(a, b, c):
     print(a*b*c)

# mul(2,2)
mul(1.1,1.1,1.1)
# mul(1,1,1)
'''

###############################################################################################
