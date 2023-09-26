import uuid

import airflow

from airflow import DAG
from airflow.decorators import task


with DAG(
    dag_id="01-dynamic-task-1",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
) as dag:

  @task
  def add(x: int, y: int):
      return x + y

  added_values = add.partial(y=10).expand(x=[1, 2, 3])