from jugador import JugadorSuperCampeon

# crear un jugador
jugador1 = JugadorSuperCampeon("Oliver Atom", 15, "Medio Campista", "Chilena")
jugador2 = JugadorSuperCampeon(
    "Steve Hiuga", 15, "Delantero", "Tiro del tigre")

print(jugador1.obtener_nombre())
print(jugador2.obtener_nombre())
jugador1.dar_pase(jugador1.obtener_nombre())
