lista_deportistas = ["Lionel Mesi", "Pele", "Simone Biles", "Rafael Nadal", "Usain Bolt", "Serena Williams", "Michael Phelps", "Cristiano Ronaldo", "Katie Ledecky"]

futbolistas = []
tenis_gimnasia = []
atletas = []

for deportista in lista_deportistas:
    if deportista in ["Lionel Mesi","Pele", "Cristiano Ronaldo"]:
        futbolistas.append(deportista)
    elif deportista in ["Simone Biles", "Rafael Nadal", "Serena Williams"]:
        tenis_gimnasia.append(deportista)
    else:
        atletas.append(deportista)

def hacer_grandioso():
    for contador in range(len(futbolistas)):
        futbolistas[contador] = "El gran " + futbolistas[contador]

def imprimir_nombres():
    for nombre in lista_deportistas:
        print(nombre)

hacer_grandioso()

print("Primer requerimiento, listar todos:")
for nombre in lista_deportistas:
    print(nombre)

print("Segundo requerimiento, listar modificados")
for nombre in futbolistas:
    print(nombre)

print("Tercer requerimiento, listar gimnastas/tenistas")
for nombre in tenis_gimnasia:
    print(nombre)

print("Cuarto requerimiento, listar restantes")
for nombre in atletas:
    print(nombre)


