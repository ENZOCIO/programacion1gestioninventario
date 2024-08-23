class Categoria:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []

    def agregarproducto(self, producto):
        if producto not in self.productos:
            self.productos.append(producto)
        else:
            print(f"El producto {producto.nombre} ya está en esta categoría.")

    def eliminarproducto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            print(f"El producto {producto.nombre} no está en esta categoría.")

    def listaproductos(self):
        return [p.nombre for p in self.productos]
