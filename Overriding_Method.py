'''
class A:
    def m1(self):
        print("M1----A")
class B(A):
      def m1(self):
          print("M1---4546546854654")


b=B()
b.m1()'''
####################################################################
# Wrong program
'''
class A:
    def __init__(self, a):
        self.a=a
        self.b=b
class B(A):
    def __init__(self,a, b, c, d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        super().__init__(self, a,b)


b=B(10, 20,10,10)
print(b)'''
#######################################################