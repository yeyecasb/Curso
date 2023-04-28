class Producto:
    def __init__(self, nombre, descripcion, precio, fecha_vencimiento):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.fecha_vencimiento = fecha_vencimiento
    
    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.precio} - {self.fecha_vencimiento}"