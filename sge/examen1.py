class A:
    pass

class B:
    pass

a = A()
b = B()
c = A()
d = a
print(a==b)
# False, porque a señala a A y 
print(a==c)
# False, porque los objetos son distintos
print(a==d)
# True, los dos señalan a la misma ud de memoria