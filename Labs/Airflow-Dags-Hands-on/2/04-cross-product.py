import uuid

import airflow

from airflow import DAG
from airflow.decorators import task


with DAG(
    dag_id="04-cross-product",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
) as dag:

    cross_product_example = BashOperator.partial(
        task_id="cross_product_example"
    ).expand(
        bash_command=[
            "echo $WORD", # prints the env variable WORD
            "echo `expr length $WORD`", # prints the number of letters in WORD
            "echo ${WORD//e/X}" # replaces each "e" in WORD with "X"
        ],
        env=[
            {"WORD": "hello"},
            {"WORD": "tea"},
            {"WORD": "goodbye"}
        ]
    )