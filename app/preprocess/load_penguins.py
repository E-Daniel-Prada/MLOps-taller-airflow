import pandas as pd
import pymysql
import os
import numpy as np
import ssl
import urllib.request


ssl._create_default_https_context = ssl._create_unverified_context

DB_HOST = "mysql"
DB_USER = "airflow"
DB_PASS = "password"
DB_NAME = "ml_db"

def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")

    # Reemplazar NaN por None para que se guarde como NULL en MySQL
    df = df.replace({np.nan: None})

    # Conectar a la base de datos
    connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
    cursor = connection.cursor()

    # Insertar datos en la base de datos
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO penguins (species, island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))
    
    connection.commit()
    connection.close()
    print("Datos de penguins cargados correctamente.")

if __name__ == "__main__":
    load_data()
