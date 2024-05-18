###################################################################################

'''
# Default parameter Method (constructor Overloading)

class A:
    def __init__(self, a, b=0):
        self.a = a
        self.b = b

    def __str__(self):
       return f" a : {self.a}, b : {self.b}"

# a1=A(10)
# print(a1)

a2=A(20,30)
print(a2)
'''


#########################################################################################################3


'''

# *a method (constructor Overloading using args)

class A:
     def __init__(self, *a):
         s=0
         for i in a:
             s=s+i
         print(s)

a=A(8,8,8)
a=A(2,2,2,2,2,2)

'''

##########################################################################################3########################################


'''

# Default parameter Method (constructor Overloading) using None

class A:
    def __init__(self, a, b=None):
        self.a=a
        self.b=b

    def __str__(self):
        return f'{self.a} , {self.b}'


a=A(10)
# print(a)

b=A(10, 20)
# print(b)

c=A(10,20,30)        #it will give error
print(c)

'''
###########################################################################################################


'''

# *a method (constructor Overloading using args)

class A:
     # def __init__(self, a,b):
     #     self.a=a
     #     self.b=b

     def __init__(self, *a ):                  #,b,c):
         #self.a=a
         s=0
         for x in a:
             s=s+x
         print("Sum :", s)
         # self.b=b
         # self.c=c

     # def display(self):
     #     print(self.a)   # self.b, self.c)
     #
     # def m1(self, c,d):
     #    print(c,d)

a=A(5,2,10)
n=A(2,2,2,2,2)
#a.display()

#a.m1(10,30)
'''

#####################################################################################################################