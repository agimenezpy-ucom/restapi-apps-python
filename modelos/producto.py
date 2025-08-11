from db.connection import conectar

class Producto:
    def __init__(self, nombre, precio, categoria_id, marca_id):
        self.nombre = nombre
        self.precio = precio
        self.categoria_id = categoria_id
        self.marca_id = marca_id

    def guardar(self):
        conn = conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO productos (nombre, precio, categoria_id, marca_id) VALUES (%s, %s, %s, %s)",
                               (self.nombre, self.precio, self.categoria_id, self.marca_id))
                conn.commit()
                cursor.close()
            except Exception as e:
                print("Error al guardar el producto:", e)
            finally:
                conn.close()

    def actualizar(self, id):
        conn = conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE productos SET nombre = %s, precio = %s, categoria_id = %s, marca_id = %s WHERE id = %s",
                               (self.nombre, self.precio, self.categoria_id, self.marca_id, id))
                conn.commit()
                cursor.close()
            except Exception as e:
                print("Error al actualizar el producto:", e)
            finally:
                conn.close()

    @staticmethod
    def obtener_todos():
        conn = conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM productos LIMIT 150")
                productos = cursor.fetchall()
                cursor.close()
                return productos
            except Exception as e:
                print("Error al obtener los productos:", e)
            finally:
                conn.close()
                
    @staticmethod
    def eliminar(id):
        conn = conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
                conn.commit()
                cursor.close()
            except Exception as e:
                print("Error al eliminar el producto:", e)
            finally:
                conn.close()