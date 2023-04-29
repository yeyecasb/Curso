from producto import Producto
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
            print("6. Salir")
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
                break
            else:
                print("Opcion incorrecta")
    
    def agregar_producto(self):
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripcion del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        fecha_vencimiento = input("Ingrese la fecha de vencimiento del producto: ")
        objeto_producto = Producto(nombre, descripcion,precio, fecha_vencimiento)
        self.tienda.agregar_item(objeto_producto)
        print("Producto agregado")
    
    def listar_producto(self):
        self.tienda.listar_items()

    def eliminar_productos(self):
        nombre=input("Ingrese el nombre del producto a eliminar: ")

        self.tienda.eliminar_item(nombre)

    def buscar_por_nombre(self):
        nombre_abarrote = input("Ingrese el nombre del producto a buscar: ")
        resultado_busqueda = self.tienda.buscar_producto(nombre_abarrote)
        if len(resultado_busqueda) == 0:
            print("No se encontro el producto")
        else:
            print(f"Se encontró el producto {nombre_abarrote}")
            for abarrote in resultado_busqueda:
                print(abarrote) #print(abarrote.nombre + " " + abarrote.precio)

    def  crear_reporte(self):
        nombre_archivo = input("Ingrese el nombre del archivo: ")
        with open(nombre_archivo, "w") as f:
            f.write("******Reporte de productos********\n")
