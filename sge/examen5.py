#HERENCIA INSTANCIAS

class A:
    pass

class B(A):
    pass

a=A()
b=B()

# a es una instancia de A
# b es una instancia de B
print(isinstance(a, A))
print(isinstance(b, B))

# Los elementos hijos con instancias
# de sus padres, pero no viceversa
print(isinstance(a, B))
print(isinstance(b, A))
# Llamamos instancia de una clase
# a todos los objetos de una clase
