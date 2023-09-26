# The following example DAG is scheduled to run every minute between its start_date and its end_date. Every DAG run contains one sensor task that will potentially take up to 20 minutes to complete.

from pendulum import datetime
from airflow import DAG
from airflow.sensors.date_time import DateTimeSensor

with DAG(
    dag_id="18-DateTimeSensor",
    start_date=datetime(2021, 12, 22, 20, 0),
    end_date=datetime(2021, 12, 22, 20, 19),
    schedule="* * * * *",
    catchup=True,
) as dag:
    sync_sensor = DateTimeSensor(
        task_id="sync_task",
        target_time="""{{ macros.datetime.utcnow() + macros.timedelta(minutes=20) }}""",
    )


# Using DateTimeSensor, one worker slot is taken up by every sensor that runs. By using the deferrable version of this sensor, DateTimeSensorAsync, you can achieve full concurrency while freeing up your workers to complete additional tasks across your Airflow environment.

# Running the DAG produces 16 running task instances, each containing one active DateTimeSensor taking up one worker slot.

# Because Airflow imposes default limits on the number of active runs of the same DAG or number of active tasks in a DAG across all runs, you'll have to scale up Airflow to concurrently run any other DAGs and tasks

