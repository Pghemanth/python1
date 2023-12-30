class Gparent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class Parent(Gparent):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c=c 
        self.d=d
class Child(Parent):
    def __init__(self,a,b,c,d,e,f):
        super().__init__(a,b,c,d) 
        self.e=e
        self.f=f
obj = Child(12,34,56,67,65,54)                      