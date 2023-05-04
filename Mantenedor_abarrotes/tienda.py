from producto import Producto
import random

class Tienda:
    def __init__(self):
        self.lista_productos = {}
    
    def agregar_item(self, clave, item):
        self.lista_productos[clave]=item
    
    def listar_items(self):
        for clave,item in self.lista_productos.items():
            print(clave, "-", item)

    def eliminar_item(self, item):
        producto_a_eliminar = []
        for abarrote in self.lista_productos:
            if abarrote.nombre == item:
                producto_a_eliminar.append(abarrote)
        
        if len(producto_a_eliminar) == 0:
            print("No se encontraron productos a eliminar")
        
        else:
            for producto in producto_a_eliminar:
                self.lista_productos.remove(producto)
            print("Producto eliminado")

    def buscar_producto(self, clave):
        productos_encontrados = {}
        for clave, abarrote in self.lista_productos.items():
            if abarrote.nombre == clave:
                productos_encontrados.append(abarrote)
        return productos_encontrados
    
    def cargar_desde_archivo(self, nombre_archivo):
        ruta_relativa = 'M3/Mantenedor_abarrotes/' + nombre_archivo
        with open(ruta_relativa, "r") as f:
            for linea in f:
                if linea != "\n":
                    clave = random.randint(0,1000)
                    campos = linea.strip().split(",")
                    nombre = campos[0]
                    descripcion = campos[1]
                    precio = float(campos[2])
                    fecha_vencimiento = campos[3]
                    obj_producto = Producto(nombre, descripcion, precio, fecha_vencimiento)
                    self.agregar_item(clave, obj_producto)
    
    def modificar_item(self, item):
        producto_encontrado = []
        for abarrote in self.lista_productos:
            if abarrote.nombre == item:
                producto_encontrado.append(abarrote)
            
        if len(producto_encontrado) == 0:
            print("No se encontraron productos")
        
        else:
            for item in producto_encontrado:
                print(f"Seleccione el parametro a modificar del producto {item}")
                print("1.- Nombre")
                print("2.- Descripcion")
                print("3.- Precio")
                print("4.- Fecha de vencimiento")
                opcion = input("Ingrese una opcion: ")
                if opcion == "1":
                    parametro = input("Ingrese el nuevo nombre: ")
                    item.nombre = parametro
                elif opcion == "2":
                    parametro = input("Ingrese la nueva descripcion: ")
                    item.descripcion = parametro
                elif opcion == "3":
                    parametro = input("Ingrese el nuevo precio: ")
                    item.precio = parametro
                elif opcion == "4":
                    parametro = input("Ingrese la nueva fecha de vencimiento: ")
                    item.vencimiento = parametro
                else:
                    print("Opcion invalida.")
                print(f"El producto se ha modificado a:  {item}")
            