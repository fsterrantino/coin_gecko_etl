from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow import DAG
import sys

from load import load
from extract import extract
from db_scripts import create_database, create_table

default_args={
    'owner': 'Fran',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='Coin_Gecko_API',
    description= 'ETL',
    start_date=datetime(2024,2,26),
    end_date=datetime(2024,2,26),
    schedule_interval='0 0 * * *'
    ) as dag:

    task1 = PythonOperator(
        task_id='create_database',
        python_callable=create_database,
        provide_context=True,
        dag=dag
    )

    task2 = PythonOperator(
        task_id='create_table',
        python_callable=create_table,
        provide_context=True,
        dag=dag
    )

    task3 = PythonOperator(
        task_id='extract_data',
        python_callable=extract,
        provide_context=True,
        dag=dag
    )

    task4 = PythonOperator(
        task_id='load_data',
        python_callable=load,
        provide_context=True,
        dag=dag
    )

task1 >> task2 >> task3
task4