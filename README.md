
# Sistema de Gestión de Productos

## Descripción

Este proyecto es un sistema de gestión de productos que permite administrar productos, categorías, bodegas, proveedores y sus relaciones. El sistema proporciona funcionalidades para el registro y gestión de estos elementos, así como para la consulta y reporte de datos.

## Requerimientos

- Python 3.8 o superior
- Flask (para la interfaz web)
- Rich (para la interfaz de texto, si se utiliza)

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd tu_repositorio
    ```

3. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    ```

4. Activa el entorno virtual:

    - En Windows:

      ```bash
      venv\Scripts\activate
      ```

    - En macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. Instala las dependencias:

    ```bash
    pip install flask rich
    ```

## Estructura del Proyecto

- `Claseproducto.py`: Definición de la clase `Producto`.
- `Clasecategoria.py`: Definición de la clase `Categoria`.
- `Clasebodega.py`: Definición de la clase `Bodega`.
- `Clasebodegaproducto.py`: Definición de la clase `BodegaProducto`.
- `Claseproveedor.py`: Definición de la clase `Proveedor`.
- `Claseproveedorproducto.py`: Definición de la clase `ProveedorProducto`.
- `main.py`: Punto de entrada de la aplicación Flask.

## Uso

1. Ejecuta la aplicación Flask:

    ```bash
    python main.py
    ```

2. Abre tu navegador web y ve a `http://127.0.0.1:5000/` para ver la aplicación en funcionamiento.

3. Para acceder a la ruta de productos, ve a `http://127.0.0.1:5000/productos`.

## Autor

Enzo Gonzalez Caicedo

## Licencia

MIT

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadida nueva característica'`).
4. Empuja tu rama (`git push origin feature/nueva-caracteristica`).
5. Crea un Pull Request.



