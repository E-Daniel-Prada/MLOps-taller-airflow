import pandas as pd
import pymysql
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Cargar variables de entorno
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

def preprocess():
    # Conectar a la base de datos y cargar los datos
    connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
    
    # Cargar datos
    df = pd.read_sql("SELECT * FROM penguins", connection)

    # Cerrar conexión con pymysql
    connection.close()

    # Limpiar datos
    df.dropna(inplace=True)  # Eliminar valores nulos

    # Codificación de variables categóricas
    df['sex'] = df['sex'].map({'MALE': 0, 'FEMALE': 1})
    df['species'] = df['species'].astype('category').cat.codes
    df['island'] = df['island'].astype('category').cat.codes
    df['bill_depth_mm'] = df['bill_depth_mm'].astype(float)

    # Evitar error de NaN en MySQL
    df.fillna(value=0, inplace=True)

    # Crear conexión SQLAlchemy para guardar datos
    engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")
    
    # Guardar datos en MySQL sin error
    df.to_sql("penguins_preprocessed", engine, if_exists="replace", index=False)

    print("Datos preprocesados y almacenados correctamente.")

if __name__ == "__main__":
    preprocess()
