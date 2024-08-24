class ProveedorProducto:
    def __init__(self, proveedor_id, producto_id, fecha_suministro):
        self.proveedor_id = proveedor_id
        self.producto_id = producto_id
        self.fecha_suministro = fecha_suministro

    @staticmethod
    def registrarsuministro(proveedor_id, producto_id, fecha_suministro):
        return ProveedorProducto(proveedor_id, producto_id, fecha_suministro)

    @staticmethod
    def listasuministrosporproveedor(proveedor_id, suministros):
        return [s for s in suministros if s.proveedor_id == proveedor_id]
