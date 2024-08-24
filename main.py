from flask import Flask, jsonify, request
from Claseproducto import Producto
from Clasecategoria import Categoria
from Clasebodega import Bodega
from Clasebodegaproducto import BodegaProducto
from Claseproveedor import Proveedor
from Claseproveedorproducto import ProveedorProducto

app = Flask(__name__)


@app.route('/productos', methods=['GET'])
def obtener_productos():

    return jsonify([])

@app.route('/productos', methods=['POST'])
def crear_producto():
    
    datos = request.json
    nuevo_producto = Producto(**datos)
   
    return jsonify({"mensaje": "Producto creado con éxito"}), 201



if __name__ == '__main__':
    app.run(debug=True)
