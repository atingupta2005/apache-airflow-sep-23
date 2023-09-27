from datetime import datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator

def _get_val(ti) -> None:
    val = ti.xcom_pull(dag_id = 'u01-2-01-dynamic-task-1', task_ids='add',key="return_value", include_prior_dates=True)
    print("val : ", val)
    if not val:
        raise ValueError('No value currently stored in XComs.')


with DAG(
    dag_id='2-worker-queue',
    schedule_interval='@daily',
    start_date=datetime(2022, 3, 1),
    catchup=False
) as dag:

    get_val = PythonOperator(
        task_id='get_val',
        python_callable=_get_val,
        queue = "spark"
    )
