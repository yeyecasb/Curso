class VehiculoMotorizado:
    def __init__(self, marca, modelo, anio, transmision, Motor):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.transmision = transmision
        self.motor = Motor

    def acelerar(self):
        if self.modelo == "Supra":
            print("Acelerando suavemente...")
        elif self.modelo == "Corolla":
            print("Acelerando con fuerza...")
        elif self.modelo == "RAV4":
            print("Acelerando con estilo...")
        elif self.marca == "Hilux":
            print("Acelerando con furia...")
        
    def obtener_informacion(self):
        print(f"Acabas de crear un vehículo Toyota modelo {self.modelo}")