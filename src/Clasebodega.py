class Bodega:
    def __init__(self, id, nombre, ubicacion, capacidad_maxima):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos = []

    def agregar_producto(self, bodega_producto):
        total_stock = sum([bp.cantidad for bp in self.productos])
        if total_stock + bodega_producto.cantidad <= self.capacidad_maxima:
            self.productos.append(bodega_producto)
        else:
            raise ValueError("No hay suficiente espacio en la bodega")

    def retirar_producto(self, bodega_producto):
        if bodega_producto in self.productos:
            self.productos.remove(bodega_producto)
        else:
            raise ValueError("El producto no se encuentra en la bodega")

    def consultar_stock(self):
        return {bp.producto_id: bp.cantidad for bp in self.productos}

    def lista_productos(self):
        return self.productos
