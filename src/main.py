from rich.console import Console
from Claseproducto import Producto
from Clasecategoria import Categoria
from Claseproveedor import Proveedor
from Clasebodega import Bodega
from Clasebodegaproducto import BodegaProducto
from Claseproveedorproducto import ProveedorProducto

console = Console()

# Simulación de bases de datos en memoria
productos = {}
categorias = {}
proveedores = {}
bodegas = {}
bodega_productos = {}
proveedor_productos = {}

def main():
    while True:
        console.print("\nMenú Principal:")
        console.print("1. Registrar Producto")
        console.print("2. Consultar Productos")
        console.print("3. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = int(input("ID del Producto: "))
            nombre = input("Nombre del Producto: ")
            descripcion = input("Descripción del Producto: ")
            precio = float(input("Precio del Producto: "))
            stock = int(input("Stock Inicial: "))
            categoria_id = int(input("ID de la Categoría: "))
            
            producto = Producto(id, nombre, descripcion, precio, stock, categoria_id)
            productos[id] = producto
            console.print("Producto registrado con éxito.")

        elif opcion == "2":
            console.print("\nListado de Productos:")
            for p in productos.values():
                console.print(f"ID: {p.id}, Nombre: {p.nombre}, Precio: {p.precio}, Stock: {p.stock}")
        
        elif opcion == "3":
            break

        else:
            console.print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
