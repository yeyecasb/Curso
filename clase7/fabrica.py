class FabricaVehiculos:
    def crear_toyota(self, modelo):
        if modelo == 'Supra':
            motor_v4 = Motor('gasolina', 4)
            return VehiculoMotorizado('Toyota', 'Supra', 1998, 'manual', motor_v4)
        elif modelo == 'Corolla':
            motor_v4 = Motor('agua', 4)
            return VehiculoMotorizado('Toyota', 'Corolla', 2022, 'automatico', motor_v4)