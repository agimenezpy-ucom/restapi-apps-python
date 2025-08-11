from db.connection import conectar

class Marca:
    def __init__(self, nombre):
        self.nombre = nombre

    def guardar(self):
        conn = conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO marcas (nombre) VALUES (%s) RETURNING id", (self.nombre,))
                conn.commit()
                self.id = cursor.fetchone()[0]
                cursor.close()
            except Exception as e:
                print("Error al guardar la marca:", e)
            finally:
                conn.close()
                
    def actualizar(self, id):
        conn = conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE marcas SET nombre = %s WHERE id = %s", (self.nombre, id))
                conn.commit()
                cursor.close()
            except Exception as e:
                print("Error al actualizar la marca:", e)
            finally:
                conn.close()

    @staticmethod
    def obtener_todas():
        conn = conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM marcas")
                marcas = cursor.fetchall()
                cursor.close()
                return marcas
            except Exception as e:
                print("Error al obtener las marcas:", e)
            finally:
                conn.close()
                
    @staticmethod
    def eliminar(id):
        conn = conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM marcas WHERE id = %s", (id,))
                conn.commit()
                cursor.close()
            except Exception as e:
                print("Error al eliminar la marca:", e)
            finally:
                conn.close()
