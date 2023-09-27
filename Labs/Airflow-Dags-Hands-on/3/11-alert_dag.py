from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta

def on_failure_dag_alert(context):
    print(f"DAG has succeeded, run_id: {context['run_id']}")

def on_success_dag_alert(context):
    print(f"DAG has failed, run_id: {context['run_id']}")


default_args =  {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Airflow',
	'retries': 3,
	'retry_delay': timedelta(seconds=60),
	'retry_exponential_backoff': False,
	'max_retry_delay': None,
	'execution_timeout': timedelta(seconds=60),
	'on_failure_callback': on_failure_dag_alert,
	'on_success_callback': on_success_dag_alert,
	'dag_timeout': timedelta(seconds=75),
}

with DAG(dag_id='11-alert_dag', schedule_interval="0 0 * * *", default_args=default_args, catchup=True) as dag:
    
    # Task 1
    t1 = BashOperator(task_id='t1', bash_command="exit 1")
    
    # Task 2
    t2 = BashOperator(task_id='t2', bash_command="sleep 45;echo 'second task'")

    t3 = BashOperator(task_id='t3', bash_command="echo 'third task'")

    t4 = BashOperator(task_id='t4', bash_command="echo 'forth task'")


    t1 >> t2 >> t3 >> t4
    