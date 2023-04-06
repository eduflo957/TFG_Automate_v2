class A:
    # Cuando inicializas en una función, la variable se
    # guarda en memoria hasta que termina de utilizarse
    a_st = 0
    # Los constructores van con __init__
    # Los constructores son una función, por ello def
    def __init__(self, a, b, c):
        # pass es cuando no quiero poner nada
        pass
        # También puedo poner el constructor si está fuera
        A.a_st=a #Te da 3
        self.b=b
        self.c=c

a = A(3,4,5)

print(A.a_st)