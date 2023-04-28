from producto import Producto
class Menu:
    def __init__(self, tienda):
        self.tienda = tienda

    def ejecutar_menu(self):
        while True:
            print("1. Agregar producto")
            print("2. Listar producto")
            print("3. Crear reporte de productos")
            print("4. Eliminar producto")
            print("5. Salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                self.agregar_producto()
            elif opcion == 2:
                self.listar_producto()
            elif opcion == 3:
                self.crear_reporte()
            elif opcion == 4:
                self.eliminar_productos()   
            elif opcion == 5:
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
