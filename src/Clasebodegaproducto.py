class BodegaProducto:
    def __init__(self, bodega_id, producto_id, cantidad, fecha_entrada):
        self.bodega_id = bodega_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.fecha_entrada = fecha_entrada

    def registrarentrada(self, cantidad, fecha_entrada):
        self.cantidad += cantidad
        self.fecha_entrada = fecha_entrada

    def registrarsalida(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
        else:
            raise ValueError("No hay suficiente stock para retirar.")
