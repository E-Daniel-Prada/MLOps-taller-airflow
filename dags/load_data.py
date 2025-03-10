from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import mysql.connector

def load_data():
    conn = mysql.connector.connect(host="mysql", user="airflow", password="airflow", database="airflow_db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tabla_destino (columna1, columna2) VALUES ('valor1', 'valor2')")
    conn.commit()
    cursor.close()
    conn.close()

default_args = {'start_date': datetime(2024, 3, 9)}
with DAG('load_data_db', default_args=default_args, schedule_interval="@daily") as dag:
    load_data_operation = PythonOperator(task_id='load_data_operation', python_callable=load_data)

