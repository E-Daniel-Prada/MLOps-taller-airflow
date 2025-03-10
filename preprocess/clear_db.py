import pymysql
import os

from dotenv import load_dotenv

# Obtener la ruta del archivo .env en la raíz del proyecto
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

# Cargar variables de entorno
load_dotenv(dotenv_path)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

def clear_database():
    connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM penguins")
    connection.commit()
    connection.close()
    print("Base de datos limpia.")

if __name__ == "__main__":
    print('Limpiando DB')
    clear_database()
