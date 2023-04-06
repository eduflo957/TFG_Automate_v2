class Sumador():
    def __init__(self, sumador):
# El sumador lo quiero guardar en la instancia
        self.sumador = sumador
    def suma(self, n):
        return self.sumador + n

# a todos los métodos se le pasa un self

# Forma corta
s = Sumador(5)
print(s.suma(3))
# Forma larga
s2 = Sumador(4)
print(Sumador.suma(s2, 2))

