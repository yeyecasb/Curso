from tienda import Tienda
from  producto import Producto
from menu import Menu

obj_tienda=Tienda()
obj_menu=Menu(obj_tienda)
obj_menu.ejecutar_menu()
