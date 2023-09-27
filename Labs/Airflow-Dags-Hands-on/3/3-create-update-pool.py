"""DAG demonstrating the umbrella use case with dummy operators."""
from airflow.models import Pool
import airflow.utils.dates
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="3-create-update-pool",
    start_date=airflow.utils.dates.days_ago(5),
    schedule_interval="@daily",
)

def _get_pools():
  # Get the pool by name
  pool = Pool.get_pool('mypool')
  
  # Now you can access the properties of the pool
  print(pool.slots)
  print(pool.occupied_slots())
  #print(pool.used_slots())
  print(pool.queued_slots())
  print(pool.open_slots())
  
def _create_pools():
  Pool.create_or_update_pool(
    "mypool",
    slots=7,
    description="Limit to 1 run of S3 ",
  )

get_pools = PythonOperator(
    task_id="get_pools", python_callable=_get_pools, dag=dag
)

create_pools = PythonOperator(
    task_id="create_pools", python_callable=_create_pools, dag=dag
)

create_pools >> get_pools


