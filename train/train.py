import pandas as pd
import pymysql
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

MODEL_PATH = "./api/models/penguin_model.pkl"

# Conectar a la base de datos y cargar los datos preprocesados
def load_data():
    connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
    df = pd.read_sql("SELECT * FROM penguins_preprocessed", connection)
    connection.close()
    return df

def train_model():
    df = load_data()

    # Separar características y etiquetas
    X = df.drop(columns=["species","id"])  # Variables de entrada
    y = df["species"]  # Variable objetivo (clasificación de la especie)

    # Dividir en datos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar un modelo Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluar el modelo
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo: {accuracy:.2f}")

    # Guardar el modelo entrenado
    with open(MODEL_PATH, "wb") as model_file:
        pickle.dump(model, model_file)

    print("Modelo guardado correctamente en 'model.pkl'.")

if __name__ == "__main__":
    train_model()
