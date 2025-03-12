# 📌 **Documentación del Proyecto: MLOPS-TALLER-AIRFLOW**  

## 📂 **Estructura del Proyecto**  

```
MLOPS-TALLER-AIRFLOW/
️ airflow/                  # Configuración y scripts de Apache Airflow
️ airflow_logs/             # Logs generados por Airflow
️ api/                      # API para servir modelos y manejar peticiones
️    ├── __pycache__/          # Archivos caché de Python
️    ├── models/               # Modelos entrenados
️    ├── dockerfile            # Dockerfile para la API
️    ├── main.py               # Punto de entrada de la API
️    └── requirements.txt      # Dependencias de la API

️ app/                      # Código principal de la aplicación
️    ├── model/                # Modelos de ML
️    ├── preprocess/           # Preprocesamiento de datos
️    │   ├── clear_db.py       # Limpieza de la base de datos
️    │   ├── dockerfile        # Dockerfile para preprocesamiento
️    │   ├── load_penguins.py  # Carga de datos de pingüinos
️    │   └── preprocess.py     # Script general de preprocesamiento
️    ├── train/                # Entrenamiento del modelo
️    │   └── train.py          # Script de entrenamiento

️ dags/                     # DAGs de Airflow
️    ├── __pycache__/          # Caché de Python
️    └── ml_pipeline.py        # Pipeline de Machine Learning en Airflow

️ env/                      # Configuración de entornos
️ logs/                     # Logs de ejecución

️ mysql/                    # Configuración de MySQL
️    └── init.sql              # Script de inicialización de la base de datos

️ plugins/                  # Plugins de Airflow
️ .env                      # Variables de entorno
️ .gitignore                # Archivos a ignorar en Git
️ docker-compose.yml        # Orquestación de servicios con Docker
️ README.md                 # Documentación del proyecto
```

---

## 🔥 **Descripción de Componentes**  

### 🔹 **1. API (`api/`)**  
Contiene el código necesario para exponer los modelos como servicio web.  

- **`main.py`**: Punto de entrada para la API.  
- **`models/`**: Carpeta donde se almacenan los modelos entrenados.  
- **`dockerfile`**: Archivo para construir la imagen Docker de la API.  
- **`requirements.txt`**: Lista de dependencias de la API.  

Ejemplo de consumo de la API

curl --location 'http://localhost:8000/predict' \
--header 'Content-Type: application/json' \
--data '{
           "bill_length_mm": 39.5,
           "bill_depth_mm": 17.4,
           "flipper_length_mm": 186,
           "body_mass_g": 3800,
           "sex": 1,
           "island": 2
}
'

Respuesta esperada

{
    "prediction": 0
}

---

### 🔹 **2. Aplicación (`app/`)**  
Aquí se encuentran los scripts para preprocesamiento, entrenamiento y gestión del modelo de Machine Learning.  

- **📂 `preprocess/`**  
  - `clear_db.py`: Script para limpiar la base de datos antes de entrenar.  
  - `load_penguins.py`: Carga de datos específicos para entrenamiento.  
  - `preprocess.py`: Transformación y limpieza de datos.  
  - `dockerfile`: Configuración Docker para preprocesamiento.  

- **📂 `train/`**  
  - `train.py`: Entrena un modelo de Machine Learning con los datos procesados.  

---

### 🔹 **3. DAGs de Airflow (`dags/`)**  
Contiene los DAGs de Apache Airflow para la orquestación del pipeline de ML.  

- **`ml_pipeline.py`**: Define el pipeline completo de ML en Airflow.  

---

### 🔹 **4. Configuración y Orquestación**  

- **`docker-compose.yml`**: Define cómo se levantan los servicios del proyecto con Docker.  
- **`mysql/init.sql`**: Script de inicialización para la base de datos MySQL.  
- **`logs/`**: Carpeta de logs generados en la ejecución del sistema.  
- **`env/`**: Configuración del entorno.  

---

## 💥 **Cómo Ejecutar el Proyecto**  

### 1️⃣ **Levantar los servicios con Docker**
```bash
docker compose build
docker compose up
```
Luego, accede a Airflow en:  
👉 **http://localhost:8080**  

