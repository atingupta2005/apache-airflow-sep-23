import uuid
from datetime import datetime
import airflow

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def sleep_function(x):
    time.sleep(x)


with DAG(
    dag_id="21-priority-pool_dag",
    start_date=datetime(2023, 1, 1),
    schedule="*/30 * * * *",
    catchup=False,
) as dag:

    task_a = PythonOperator(
        task_id="task_a",
        python_callable=sleep_function,
        pool="mypool",
        op_args=[5],
        pool_slots = 1,
    )

    task_b = PythonOperator(
        task_id="task_b",
        python_callable=sleep_function,
        pool="mypool",
        priority_weight=2,
        pool_slots = 2,
        op_args=[10],
    )
