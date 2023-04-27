# es inmutable
tupla_vacia = ()
power_rangers = ('red', 'yellow', 'black')
tupla2 = "uno", "dos", "tres"

# power_rangers[0] = 'blue'

lista_super = ['Bebida', 'Huevos', 'Aceite', 'Sal', 'Limon']

nueva_tupla = tuple(lista_super)
print(nueva_tupla)

p1, p2, p3, p4, p5 = nueva_tupla  # desempaquetamiento de tupla

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

# tupla utiliza menos espacio que una lista
# la tupla ofrece proteccion a cambios no planeados
