# continue con flash
print("Flash empezo a correr para derrotar enemigos")
print("Que enemigo estan actualmente corriendo?")

corredores = ["Zoom", "flash reverso", "la muerte", "Savitar", "kid flash"]

for corredor in corredores:
    if corredor == "la muerte":
        print("Flash encontro a la muerte")
        continue
        print("La muerte destruyo a flash")
        break
    else:
        print("Flash vencio a ", corredor)

print("Grande flash")
