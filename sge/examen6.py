# HERENCIA - MÉTODOS

class A:
    def __init__(self,a):
        self.a=a

    def get_a(self):
        return self.a

class B(A):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_b(self):
        return self.b

# Todo lo que pongas de B, te lo hereda de A
# Pero si sobreescribes en B, prima B antes que A

# Como tiene 2 parámetros, lo podemos llamar con 1
a = A(1)
print(a.get_a()) #Me sale 1

b = B(8,2)
print(b.get_b())

# Pregunta de examen:
print(b.get_a()) #Si puede porque se heredan los métodos
#Coge el elemento a de la clase B