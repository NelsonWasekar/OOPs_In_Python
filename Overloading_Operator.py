
print(1+2)



#####################################################################################################################

'''
class A:
     def __init__(self, x):
          self.x=x


a=A(50)
a1=A(100)
print(a+a1)
'''

#####################################################################################################################
'''

# Addition of Two Objects

class A:
     def __init__(self, x):
         self.x=x

     def __add__(self, other):
         return self.x+other.x
           # return f'{self.x}+{other.x}'

a=A(10)
a1=A(20)
print(a+a1)
# a2=A(10)
# a3=A(10)
# print(a+a1)
# print(A(a+a1)+a2)
#
# a4=A(20)
# print(A(a+a1)+A(a3+a4))

'''
##################################################################################################################


'''
#Multiplication of two Objects

class A:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        return self.x * other.x

a=A(10)
a1=A(5)
print(a*a1)

a3=A(2)
print(A(a*a1)*a3)
'''

#############################################################################################################

'''
# Division Operator

class D:
     def __init__(self, a):
         self.a=a

     def __truediv__(self, other):
         Q=self.a/other.a
         R=self.a/other.a
         return f"Quotient : {Q}, Remainder : {R} "

d1=D(10)
d2=D(5)
print(d1/d2)
'''

########################################################################################################################

'''
# Floor Division


class D:
    def __init__(self, a):
        self.a=a

    def __floordiv__(self, other):
        Q=self.a//other.a
        R=self.a//other.a
        print("Quotient : ", Q)
        print("Remainder : ", R)

d1=D(10)
d2=D(5)
(d1//d2)
'''
########################################################################
'''
# Power Operator
class P:
    def __init__(self, a):
        self.a = a

    def __pow__(self, other):
         p=(self.a)**(other.a)
         return p

p1=P(5)
p2=P(2)
print(p1**p2)
'''
#################################################################
'''
# Right Shift

class R:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        b =self.a > other.a
        return b
r1=R(50)
r2=R(60)

print(r1>r2)
'''
#######################################################################################


############################################################################################
'''
class A:
      def __init__(self, x):
          self.x=x
      def __mul__(self, other):
          return self.x * other.x

a=A(2)
a1=A(2)
a2=A(5)
print(A(a*a1)*a2)
'''
#############################################################################################

'''
class A:
    def __init__(self, a):
        self.a=a

    def __add__(self, other):
        return self.a+other.a

a=A(10)
a1=A(20)

print(a+a1)'''

###############################################################################






