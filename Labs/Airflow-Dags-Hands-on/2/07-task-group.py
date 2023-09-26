from airflow.models import DAG
from airflow.operators.python import task
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup

@task
def show():
    print("Python is awesome")

with DAG(
    dag_id="07-task-group",
    default_args={'owner': 'airflow'},
    start_date=days_ago(2),
    schedule_interval=None,
) as dag3:

    with TaskGroup(group_id="tasks_1") as tg1:
        for _ in range(10):
            BashOperator(task_id=f'processing_{_}', bash_command='ls')