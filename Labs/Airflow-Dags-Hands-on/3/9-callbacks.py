import datetime
import pendulum

from airflow import DAG
from airflow.operators.empty import EmptyOperator


def task_failure_alert(context):
    print(f"Task has failed, task_instance_key_str: {context['task_instance_key_str']}")


def dag_failure_alert(context):
    print(f"DAG has failed, run_id: {context['run_id']}")


def dag_success_alert(context):
    print(f"DAG has succeeded, run_id: {context['run_id']}")


def dag_execute_alert(context):
    print(f"DAG has executed, run_id: {context['run_id']}")

def task_failure_alert(context):
    print(f"Task has failed, task_instance_key_str: {context['task_instance_key_str']}")

with DAG(
    dag_id="9-callbacks",
    schedule=None,
    start_date=pendulum.datetime(2023, 1, 1),
    dagrun_timeout=datetime.timedelta(minutes=60),
    catchup=False,
    on_success_callback=None,
    on_failure_callback=task_failure_alert,
    tags=["example"],
):

    task1 = EmptyOperator(task_id="task1", on_execute_callback=[dag_execute_alert])
    task2 = EmptyOperator(task_id="task2", on_failure_callback=[dag_failure_alert])
    task3 = EmptyOperator(task_id="task3", on_success_callback=[dag_success_alert])
    task1 >> task2 >> task3