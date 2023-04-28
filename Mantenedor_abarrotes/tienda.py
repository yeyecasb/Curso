from producto import Producto

class Tienda:
    def __init__(self):
        self.lista_productos = []
    
    def agregar_item(self, item):
        self.lista_productos.append(item)
    
    def listar_items(self):
        for item in self.lista_productos:
            print(item)

    def eliminar_item(self, item):
        self.lista_productos.remove(item)