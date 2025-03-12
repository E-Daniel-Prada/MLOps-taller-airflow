from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def clear_db():
    subprocess.run(["python", "/opt/airflow/app/preprocess/clear_db.py"], check=True)

def load_penguins():
    subprocess.run(["python", "/opt/airflow/app/preprocess/load_penguins.py"], check=True)

def preprocess():
    subprocess.run(["python", "/opt/airflow/app/preprocess/preprocess.py"], check=True)

def train_model():
    subprocess.run(["python", "/opt/airflow/app/train/train.py"], check=True)


with DAG(
    dag_id="ml_pipeline",
    schedule_interval="@daily",
    start_date=datetime(2024, 3, 1),
    catchup=False
) as dag:
    
    task_clear_db = PythonOperator(
        task_id="clear_db",
        python_callable=clear_db
    )
    
    task_load_data = PythonOperator(
        task_id="load_penguins",
        python_callable=load_penguins
    )
    
    task_preprocess = PythonOperator(
        task_id="preprocess",
        python_callable=preprocess
    )
    
    task_train = PythonOperator(
        task_id="train_model",
        python_callable=train_model
    )
    
    
    task_clear_db >> task_load_data >> task_preprocess >> task_train
