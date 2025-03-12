from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel
import os

# Cargar el modelo entrenado
MODEL_PATH = "models/penguin_model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"No se encontró el modelo en {MODEL_PATH}. Asegúrate de entrenarlo antes de usar la API.")

with open(MODEL_PATH, "rb") as model_file:
    model = pickle.load(model_file)

app = FastAPI(title="API de Predicción de Penguins")

# Definir el esquema de entrada
class PenguinInput(BaseModel):
    island: int
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: int
    body_mass_g: int
    sex: int
    

@app.get("/")
def root():
    return {"message": "API de inferencia para clasificación de Penguins"}

@app.post("/predict")
def predict(penguin: PenguinInput):
    try:
        # Convertir los datos de entrada en un DataFrame
        data = pd.DataFrame([penguin.dict()])

        # Hacer la predicción
        prediction = model.predict(data)[0]

        # Convertir la predicción a int nativo si es un numpy.int64
        return {"prediction": int(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
