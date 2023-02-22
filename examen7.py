# GENERADORES

# Esta función no genera 1millón de números
# Pasa la información, pero sólo los crea cuando los va a utilizar

def gen_numbers(n):
    for i in range(n):
        yield i

g = gen_numbers(5)
print(next(g))
print(next(g))
print(list(g))