class Bodega:
    def __init__(self, id, nombre, ubicacion, capacidad_maxima):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos = []

    def agregarproducto(self, producto, cantidad):
        if self.capacidad_disponible() >= cantidad:
            self.productos.append((producto, cantidad))
        else:
            raise ValueError("No hay suficiente capacidad en la bodega.")

    def retirarproducto(self, producto, cantidad):
        for p in self.productos:
            if p[0] == producto:
                if p[1] >= cantidad:
                    p[1] -= cantidad
                    if p[1] == 0:
                        self.productos.remove(p)
                else:
                    raise ValueError("No hay suficiente stock del producto en la bodega.")
                break

    def consultarstock(self):
        return {p[0]: p[1] for p in self.productos}

    def listaproductos(self):
        return [(p[0].nombre, p[1]) for p in self.productos]

    def capacidad_disponible(self):
        ocupada = sum([p[1] for p in self.productos])
        return self.capacidad_maxima - ocupada
