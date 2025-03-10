from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import mysql.connector

def clean_db():
    conn = mysql.connector.connect(host="mysql", user="airflow", password="airflow", database="airflow_db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tabla_destino")
    conn.commit()
    cursor.close()
    conn.close()

default_args = {'start_date': datetime(2024, 3, 9)}
with DAG('delete_data_db', default_args=default_args, schedule_interval="@daily") as dag:
    delete_data = PythonOperator(task_id='clean_data_db', python_callable=clean_db)
