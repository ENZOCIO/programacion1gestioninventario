class Producto:
    def __init__(self, id, nombre, descripcion, precio, stock, categoria_id):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria_id = categoria_id

    def añadir_stock(self, cantidad):
        self.stock += cantidad

    def retirar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            raise ValueError("No hay suficiente stock disponible")

    def consultar_stock(self):
        return self.stock

    def consultar_valor_total_stock(self):
        return self.precio * self.stock

    def cambiar_categoria(self, nueva_categoria_id):
        self.categoria_id = nueva_categoria_id

    def asignar_proveedor(self, proveedor_producto):
        pass

    def eliminar_proveedor(self, proveedor_producto):
        pass
