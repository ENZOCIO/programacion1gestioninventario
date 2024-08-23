class Proveedor:
    def __init__(self, id, nombre, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = []

    def agregarproducto(self, producto):
        if producto not in self.productos:
            self.productos.append(producto)
        else:
            print(f"El producto {producto.nombre} ya está en la lista de productos del proveedor.")

    def eliminarproducto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            print(f"El producto {producto.nombre} no está en la lista de productos del proveedor.")

    def listaproductos(self):
        return [p.nombre for p in self.productos]
