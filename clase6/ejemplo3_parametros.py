# atributos nominal

# atributos posicionales de los parametros


def atacar(nombre_ataque, poder_ataque, enemigo):
    print("Goku ha usado", nombre_ataque, "con un poder de: ",
          poder_ataque, "contra ", enemigo)


def defender(enemigo, movimiento="Esquivar"):
    print("goku eligio ", movimiento, "para enfrentar a ", enemigo)


defender("magin bu", "contraatacar")

# atacar("vegeta", 8000, "kame hame")

# parametros nominales


def atacar_nominal(nombre_ataque, poder_ataque, enemigo):
    print("Goku ha usado", nombre_ataque, "con un poder de: ",
          poder_ataque, "contra ", enemigo)


atacar_nominal(poder_ataque="8000", enemigo="Vegeta",
               nombre_ataque="kame hame")
