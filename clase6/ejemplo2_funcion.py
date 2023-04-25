# retornos de none, cuando no retornamos nada en la funcion

def accion():
    x = 0


# en este caso retorna None
print(accion())

# retornar multiples valores


def multiple():
    return 0, 1, 2, 3


resultado = multiple()  # recibimos una tupla
print(resultado)
print(type(resultado))

# desempaquetado de tupla
a, b, c, d = multiple()
print(a)
print(b)
