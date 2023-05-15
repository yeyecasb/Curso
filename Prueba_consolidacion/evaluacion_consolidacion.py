lista_de_nombres = ['Harry Houdini','Newton','David Blaine','Hawking','Messi','Teller','Einstein','Pele','Juanes']

magos = []
cientificos = []
otros = []

for nombre in lista_de_nombres:
    if nombre in ['Harry Houdini','David Blaine','Teller']:
        magos.append(nombre)
    elif nombre in ['Newton','Hawking','Einstein']:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

def hacer_grandioso():
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

def imprimir_nombres():
    for nombre in lista_de_nombres:
        print(nombre)

print("Lista completa")
imprimir_nombres()
print("")

print("Lista de magos")
hacer_grandioso()
for nombre in magos:
    print(nombre)
print("")

print("Lista de cientificos")
for nombre in cientificos:
    print(nombre)
print("")

print("Lista de otros")
for  nombre in otros:
    print(nombre)
print("")



