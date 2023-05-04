from producto import Producto
import random
class Menu:
    def __init__(self, tienda):
        self.tienda = tienda

    def ejecutar_menu(self):
        while True:
            print("1. Agregar producto")
            print("2. Listar producto")
            print("3. Crear reporte de productos")
            print("4. Buscar producto por nombre")
            print("5. Eliminar producto")
            print("6. Modificar un producto")
            print("7. Cargar masiva de productos")
            print("8. Salir")
            
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                self.agregar_producto()
            elif opcion == 2:
                self.listar_producto()
            elif opcion == 3:
                self.crear_reporte()
            elif opcion == 4:
                self.buscar_por_nombre()
            elif opcion == 5:
                self.eliminar_productos()   
            elif opcion == 6:
                self.modificar_producto()
            elif opcion == 7:
                self.carga_masiva()
            elif opcion == 8:
                break
            else:
                print("Opcion incorrecta")
    
    def agregar_producto(self):
        clave = random.randint(1,1000)
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripcion del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        fecha_vencimiento = input("Ingrese la fecha de vencimiento del producto: ")
        objeto_producto = Producto(nombre, descripcion,precio, fecha_vencimiento)
        self.tienda.agregar_item(clave, objeto_producto)
        print("Producto agregado")
    
    def listar_producto(self):
        self.tienda.listar_items()

    def eliminar_productos(self):
        nombre=input("Ingrese el nombre del producto a eliminar: ")
        self.tienda.eliminar_item(nombre)
        

    def buscar_por_nombre(self):
        clave_abarrote = input("Ingrese la ID del producto a buscar: ")
        resultado_busqueda = self.tienda.buscar_producto(clave_abarrote)
        if len(resultado_busqueda) == 0:
            print("No se encontro el producto")
        else:
            print(f"Se encontró el producto {nombre_abarrote}")
            for clave, abarrote in resultado_busqueda.items():
                print(clave, abarrote) #print(abarrote.nombre + " " + abarrote.precio)

    def  crear_reporte(self):
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        with open(nombre_archivo, "w") as f:
            f.write("******Reporte de productos********\n")
            #f.write(self.listar_producto() + "\n")
            for producto in self.tienda.lista_productos:
                f.write(str(producto) + "\n")
        print(f"Reporte {nombre_archivo} generado con exito")

    def carga_masiva(self):
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        self.tienda.cargar_desde_archivo(nombre_archivo)

    def modificar_producto(self):
        nombre =  input("Ingrese el nombre del producto a modificar: ")
        self.tienda.modificar_item(nombre)
