import pymysql
import os

DB_HOST = "mysql"
DB_USER = "airflow"
DB_PASS = "password"
DB_NAME = "ml_db"

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
