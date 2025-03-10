# MLAIRFLOW

Un proyecto de Machine Learning con Airflow, API, MySQL y procesamiento de datos.

## 📂 Estructura del Proyecto

```
MLAIRFLOW/
│── airflow/
│   ├── dags/
│   │   └── ml_pipeline.py  # DAG de Airflow para el pipeline de ML
│   ├── dockerfile          # Contenedor de Airflow
│   └── requirements.txt    # Dependencias de Airflow
│
│── airflow_logs/scheduler/
│   ├── 2025-03-07/         # Logs del scheduler de Airflow
│   └── latest              # Último log del scheduler
│
│── api/
│   ├── __pycache__/        # Caché de Python
│   ├── models/
│   │   └── penguin_model.pkl  # Modelo entrenado en formato Pickle
│   ├── deploy.py           # Script de despliegue de la API
│   ├── dockerfile          # Contenedor de la API
│   ├── main.py             # Código principal de la API
│   └── requirements.txt    # Dependencias de la API
│
│── env/                    # Configuración de entorno
│
│── mysql/
│   └── init.sql            # Script de inicialización de MySQL
│
│── preprocess/
│   ├── clear_db.py         # Limpieza de la base de datos
│   ├── dockerfile          # Contenedor de preprocesamiento
│   ├── load_penguins.py    # Carga de datos
│   ├── preprocess.py       # Preprocesamiento de datos
│   └── requirements.txt    # Dependencias de preprocesamiento
│
│── train/
│   ├── models/             # Carpeta de modelos entrenados
│   ├── dockerfile          # Contenedor del entrenamiento
│   ├── requirements.txt    # Dependencias del entrenamiento
│   ├── train.py            # Script de entrenamiento del modelo
│
└── .env                    # Variables de entorno
```

---

## 🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPO>
   cd MLAIRFLOW
   ```

2. Configura las variables de entorno:
   ```bash
   cp .env.example .env
   ```

3. Construye los contenedores Docker:
   ```bash
   docker-compose up --build
   ```

---

## 🛠️ Componentes Principales

### 1️⃣ **Airflow**
- Ejecuta y gestiona pipelines de ML.
- DAG principal: `ml_pipeline.py`.

### 2️⃣ **API**
- Sirve el modelo entrenado `penguin_model.pkl`.
- Despliegue en `deploy.py`.

### 3️⃣ **Base de Datos (MySQL)**
- Base de datos para almacenamiento de datos procesados.
- Script de inicialización: `init.sql`.

### 4️⃣ **Preprocesamiento**
- `preprocess.py`: Limpieza y transformación de datos.
- `load_penguins.py`: Carga de datos.

### 5️⃣ **Entrenamiento**
- `train.py`: Entrena el modelo de ML.
- Modelos guardados en `train/models/`.

---

## 📜 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

---
