from fabrica import FabricaVehiculos #fabrica.py

mi_fabrica = FabricaVehiculos()

vehiculo1 = mi_fabrica.crear_toyota('Supra')
vehiculo2 = mi_fabrica.crear_toyota('Corolla')

vehiculo2.acelerar()
vehiculo2.obtener_informacion()