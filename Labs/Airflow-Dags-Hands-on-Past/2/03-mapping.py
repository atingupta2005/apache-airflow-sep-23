import uuid

import airflow

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


with DAG(
    dag_id="03-mapping",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
) as dag:

   def one_two_three_traditional():
       return [1, 2, 3]

   @task
   def plus_10_TF(x):
       return x + 10

   one_two_three_task = PythonOperator(
       task_id="one_two_three_task", python_callable=one_two_three_traditional
   )

   plus_10_TF.partial().expand(x=one_two_three_task.output)