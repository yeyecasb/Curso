# Búsqueda de elementos: Escribe un programa que tome una lista de nombres como
# entrada y pregunte al usuario si un nombre específico se encuentra en la lista.
nombres=['Juan','Pedro','Diego','Claudio']
eleccion_usuario=input('Ingrese nombre a buscar : ')
print('El nombre buscado está en la posición: ',nombres.index(eleccion_usuario))