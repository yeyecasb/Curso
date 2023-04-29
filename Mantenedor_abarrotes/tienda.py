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

    def buscar_producto(self, item):
        productos_encontrados = []
        for abarrote in self.lista_productos:
            if abarrote.nombre == item:
                productos_encontrados.append(abarrote)
        return productos_encontrados
    
    def cargar_desde_archivo(self, nombre_archivo):
        ruta_relativa = 'M3/Mantenedor_abarrotes/' + nombre_archivo
        with open(ruta_relativa, "r") as f:
            for linea in f:
                if linea != "\n":
                    campos = linea.strip().split(",")
                    nombre = campos[0]
                    descripcion = campos[1]
                    precio = float(campos[2])
                    fecha_vencimiento = campos[3]
                    obj_producto = Producto(nombre, descripcion, precio, fecha_vencimiento)
                    self.agregar_item(obj_producto)
            