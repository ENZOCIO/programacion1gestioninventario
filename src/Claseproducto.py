class Producto:
    def __init__(self, id, nombre, descripcion, precio, stock, categoria):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        self.proveedores = []

    def añadirstock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
        else:
            raise ValueError("La cantidad a agregar debe ser mayor que 0.")

    def retirarstock(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.stock:
                self.stock -= cantidad
            else:
                raise ValueError("No hay suficiente stock para retirar.")
        else:
            raise ValueError("La cantidad a retirar debe ser mayor que 0.")

    def consultarstock(self):
        return self.stock

    def consultarvalortotalstock(self):
        return self.stock * self.precio

    def cambiarcategoria(self, nueva_categoria):
        self.categoria = nueva_categoria

    def asignarproveedor(self, proveedor):
        if proveedor not in self.proveedores:
            self.proveedores.append(proveedor)
        else:
            print(f"El proveedor {proveedor} ya está asociado a este producto.")

    def eliminarproveedor(self, proveedor):
        if proveedor in self.proveedores:
            self.proveedores.remove(proveedor)
        else:
            print(f"El proveedor {proveedor} no está asociado a este producto.")
