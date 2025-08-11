import psycopg2
import os 

def conectar():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("APP_DATABASE", "test"),
            user=os.getenv("APP_USER", "dummy"),
            password=os.getenv("APP_PASSWORD", "12345"),
            host=os.getenv("APP_HOST", "localhost"),
            options="-c client_encoding=utf8"
        )
        return conn
    except psycopg2.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None
