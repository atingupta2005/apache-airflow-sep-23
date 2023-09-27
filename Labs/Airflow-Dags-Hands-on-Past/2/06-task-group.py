import uuid

import airflow

from airflow import DAG
from airflow.decorators import task,task_group
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="06-task-group",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
) as dag:
     @task_group(
         group_id="task_group_1",
         default_args={"conn_id": "postgres_default"},
         tooltip="This task group is very important!",
         prefix_group_id=True,
         # parent_group=None,
         # dag=None,
     )
     def tg1():
         t1 = EmptyOperator(task_id="t1")

     tg1()