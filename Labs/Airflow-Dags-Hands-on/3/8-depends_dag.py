from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2032, 8, 8),
    'owner': 'Airflow',
    wait_for_downstream=True
}

def second_task():
    print('Hello from second_task')
    #raise ValueError('This will turns the python task in failed state')

def third_task():
    print('Hello from third_task')
    #raise ValueError('This will turns the python task in failed state')

with DAG(dag_id='depends_task', schedule_interval="0 0 * * *", default_args=default_args) as dag:
    
    # Task 1
    bash_task_1 = BashOperator(task_id='bash_task_1', bash_command="echo 'first task'")
    
    # Task 2
    python_task_2 = PythonOperator(task_id='python_task_2', python_callable=second_task, depends_on_past= True)

    # Task 3
    python_task_3 = PythonOperator(task_id='python_task_3', python_callable=third_task, depends_on_past= False)

    # Task 4
    python_task_4 = PythonOperator(task_id='python_task_4', python_callable=third_task, depends_on_past= True)


    bash_task_1 >> python_task_2 >> python_task_3

    # depends_on_past — If set to true, the task in the current DAG run will only run if the same task succeeded or was skipped in the previous run.

    # wait_for_downstream — If set to true, the task in the current run will only run if the same task succeeded or skipped in the previous run and the immediate downstream task in the previous run also succeeded or was skipped.
