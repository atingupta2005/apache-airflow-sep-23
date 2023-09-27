import uuid

import airflow
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from airflow import DAG
from airflow.decorators import task


with DAG(
    dag_id="05-set-of-keyword-arguements",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
) as dag:

   # input sets of kwargs provided directly as a list[dict]
   t1 = BashOperator.partial(task_id="t1").expand_kwargs(
       [
           {"bash_command": "echo $WORD", "env" : {"WORD": "hello"}},
           {"bash_command": "echo `expr length $WORD`", "env" : {"WORD": "tea"}},
           {"bash_command": "echo ${WORD//e/X}", "env" : {"WORD": "goodbye"}}
       ]
   )