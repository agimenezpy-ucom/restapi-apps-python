from flask import Flask, request, jsonify
from modelos.categoria import Categoria
from modelos.producto import Producto
from modelos.marca import Marca

app = Flask(__name__)

# Configurar la aplicación para usar UTF-8
app.config['JSON_AS_ASCII'] = False

# Manejar solicitudes relacionadas con categorías
@app.route('/categorias', methods=['GET', 'POST'])
def manejar_categorias():
    if request.method == 'GET':
        categorias = Categoria.obtener_todas()
        return jsonify(categorias)
    elif request.method == 'POST':
        datos = request.json
        nueva_categoria = Categoria(nombre=datos['nombre'])
        nueva_categoria.guardar()
        return jsonify({"mensaje": "Categoria creada exitosamente", "categoria": vars(nueva_categoria)}), 201
    
@app.route('/categorias/<int:id>', methods=['PUT', 'DELETE'])
def manipular_categoria(id):
    if request.method == 'PUT':
        datos = request.json
        categoria_actualizada = Categoria(nombre=datos['nombre'])
        categoria_actualizada.actualizar(id)
        return jsonify({"mensaje": "Categoría actualizada exitosamente"})
    elif request.method == 'DELETE':
        Categoria.eliminar(id)
        return jsonify({"mensaje": "Categoría eliminada exitosamente"})   
    
# Manejar solicitudes relacionadas con marcas
@app.route('/marcas', methods=['GET', 'POST'])
def manejar_marcas():
    if request.method == 'GET':
        marcas = Marca.obtener_todas()
        return jsonify(marcas)
    elif request.method == 'POST':
        datos = request.json
        nueva_marca = Marca(nombre=datos['nombre'])
        nueva_marca.guardar()
        return jsonify({"mensaje": "Marca creada exitosamente", "marca": vars(nueva_marca)}), 201
    
@app.route('/marcas/<int:id>', methods=['PUT', 'DELETE'])
def manipular_marca(id):
    if request.method == 'PUT':
        datos = request.json
        marca_actualizada = Categoria(nombre=datos['nombre'])
        marca_actualizada.actualizar(id)
        return jsonify({"mensaje": "Marca actualizada exitosamente"})
    elif request.method == 'DELETE':
        Marca.eliminar(id)
        return jsonify({"mensaje": "Marca eliminada exitosamente"})        

# Manejar solicitudes relacionadas con productos
@app.route('/productos', methods=['GET', 'POST'])
def manejar_productos():
    if request.method == 'GET':
        productos = Producto.obtener_todos()
        return jsonify(productos)
    elif request.method == 'POST':
        datos = request.json
        nuevo_producto = Producto(nombre=datos['nombre'], precio=datos['precio'], categoria_id=datos['categoria_id'], marca_id=datos['marca_id'])
        nuevo_producto.guardar()
        return jsonify({"mensaje": "Producto creado exitosamente"}), 201
    
@app.route('/productos/<int:id>', methods=['PUT', 'DELETE'])
def manipular_producto(id):
    if request.method == 'PUT':
        datos = request.json
        producto_actualizado = Producto(nombre=datos['nombre'], precio=datos['precio'], categoria_id=datos['categoria_id'], marca_id=datos['marca_id'])
        producto_actualizado.actualizar(id)
        return jsonify({"mensaje": "Producto actualizado exitosamente"})
    elif request.method == 'DELETE':
        Producto.eliminar(id)
        return jsonify({"mensaje": "Producto eliminado exitosamente"})    

if __name__ == '__main__':
    app.run(debug=False)
