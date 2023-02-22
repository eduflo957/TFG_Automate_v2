# MIEMBROS

class A:
    def __init__(self,b):
        self.b = b

class B:
    pass

b = B()
a = A(b)

print(a)
print(b)
print(a.b)

####### Una clase siempre puede tener un objeto de otra clase