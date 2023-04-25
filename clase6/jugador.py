#
# definir una clase

class JugadorSuperCampeon:
    # constructor
    def __init__(self, nombre, edad, posicion, habilidad):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.habilidad = habilidad

    def obtener_nombre(self):
        esta_contratado = True
        n = self.nombre
        if esta_contratado:
            return n
        else:
            return "desconocido"

    def hacer_jugada(self):
        print('el jugador esta corriendo por la banda')

    def dar_pase(self, compañero):
        print('dando el pase a', compañero)
