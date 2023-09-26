import uuid

import airflow

from airflow import DAG
from airflow.decorators import task


with DAG(
    dag_id="02-mapping",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
) as dag:

  @task
  def one_two_three_TF():
      return [1, 2, 3]

  @task
  def plus_10_TF(x):
      return x + 10

  plus_10_TF.partial().expand(x=one_two_three_TF())