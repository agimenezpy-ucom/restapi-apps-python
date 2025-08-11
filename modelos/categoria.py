from db.connection import conectar

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def guardar(self):
        conn = conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO categorias (nombre) VALUES (%s) RETURNING id", (self.nombre,))
                conn.commit()
                self.id = cursor.fetchone()[0]
                cursor.close()
            except Exception as e:
                print("Error al guardar la categoría:", e)
            finally:
                conn.close()
                
    def actualizar(self, id):
        conn = conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE categorias SET nombre = %s WHERE id = %s", (self.nombre, id))
                conn.commit()
                cursor.close()
            except Exception as e:
                print("Error al actualizar la categoria:", e)
            finally:
                conn.close()

    @staticmethod
    def obtener_todas():
        conn = conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM categorias")
                categorias = cursor.fetchall()
                cursor.close()
                return categorias
            except Exception as e:
                print("Error al obtener las categorias:", e)
            finally:
                conn.close()
                
    @staticmethod
    def eliminar(id):
        conn = conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM categorias WHERE id = %s", (id,))
                conn.commit()
                cursor.close()
            except Exception as e:
                print("Error al eliminar la categoria:", e)
            finally:
                conn.close()
