'''
# Without Inheritance

class A:
    def m1(self):
        print("m1____A")

class B:
    def m2(self):
        print("m2____B")

b=B()
# b.m1()

# b=B()
# b.m2()
# b.m1()
'''
#################################################################################################
'''
class A:
    def m1(self):
        print("M1---A")
class B(A):
     def m2(self):
        print("M2___B")

b=B()
b.m2()
# b.m1()

'''
#################################################################################################
'''
class A:
    def __init__(self, x):
        self.x=x
class B(A):
   pass

#b=B()
b=B(5)
'''
################################################################################################

'''
class A:
    def __init__(self, x):
        self.x=x
        
class B(A):
    def __init__(self):
       # print("Constructor B")
       pass
    
b=B()
'''

#################################################################################################

'''
class A:
    def __init__(self, x):
        self.x = x
        #print("Constructor A")

class B(A):
    def __init__(self):
        print("Constructor B")


b=B()
'''
##############################################################################################
'''
class A:
    pass
class B(A):
    pass
b=B()

'''
############################################################################################
'''
# Without Inheritance
class A:
    pass
class B:
    def __init__(self, x, y):
        self.x=x
        self.y=y
b=B(5,4)
'''
#######################################################################################3

'''
# Using Super Keyword  (Relation Ship Mandatory)

class A:
     def __init__(self):
         print("Constructor A")
class B(A):
     def __init__(self):
        print("Constructor B")
        super().__init__()
        A.__init__(self)

b=B()
print(B.mro())

'''
##################################################################################################

'''

# class A and class B ( Relationship Not Required)
class A:
     def __init__(self):
         print("Constructor A")
class B:
     def __init__(self):
        print("Constructor B")
        A.__init__(self)
        super.__init__(self)

b=B()
'''
##################################################################################################

'''
class A:
    pass
class B:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        print("Nelson")

b=B(5,4)

'''

#####################################################################################################