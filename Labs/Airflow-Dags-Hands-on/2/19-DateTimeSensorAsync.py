# Switching out the DateTimeSensor for DateTimeSensorAsync will create 16 running DAG instances, but the tasks for these DAGs are in a deferred state which does not take up a worker slot. The only difference in the DAG code is using the deferrable operator DateTimeSensorAsync over DateTimeSensor:

from pendulum import datetime
from airflow import DAG
from airflow.sensors.date_time import DateTimeSensorAsync

with DAG(
    dag_id="async_dag_2",
    start_date=datetime(2021, 12, 22, 20, 0),
    end_date=datetime(2021, 12, 22, 20, 19),
    schedule="* * * * *",
    catchup=True,
) as dag:
    async_sensor = DateTimeSensorAsync(
        task_id="async_task",
        target_time="""{{ macros.datetime.utcnow() + macros.timedelta(minutes=20) }}""",
    )

# In the UI, all tasks are shown in a deferred (violet) state. Tasks in other DAGs can use the available worker slots, making the deferrable operator more cost and time-efficient.