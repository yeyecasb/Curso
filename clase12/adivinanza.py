import random
intentos = 0
numero_en_mente = random.randint(1,100)

print("Bienvenido al juego de adivinar el numero")
print("Pensé un numero entre 1 y 100, adivina cuál es...")

while True:
    intentos += 1
    numero_ingresado = int(input("Ingresa tu numero: "))
    if numero_ingresado < numero_en_mente:
        print("El numero que tengo en mente es mayor que ",numero_ingresado)
    elif numero_ingresado > numero_en_mente:
        print("El numero que tengo en mente es menor que ",numero_ingresado)
    else:
        print("Felicidades, has ganado")
        print("Lo lograste en", intentos, "intentos")
        break