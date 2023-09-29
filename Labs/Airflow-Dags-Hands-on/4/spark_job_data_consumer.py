import asyncio
from concurrent.futures import ThreadPoolExecutor
from airflow.sensors.base import BaseSensorOperator
from airflow.models.baseoperator import BaseOperator
import os
from datetime import datetime
from airflow.decorators import dag, task
from airflow.triggers.base import BaseTrigger, TriggerEvent
from typing import Any
from typing import Dict, Tuple
from airflow import DAG
from airflow.operators.python import PythonOperator
import platform

class SuccessFileTrigger(BaseTrigger):
    def __init__(self, file_input_directory: str):
        super().__init__()
        print(f"Starting __init__")
        self.file_found = False
        self.file_input_directory = file_input_directory
        self.file_to_wait_for = f'{file_input_directory}/_SUCCESS'
        print(f"File not found-{self.file_to_wait_for}")
        print("platform: ", platform.node())
        print(f"Stopping __init__")

    def _check_if_file_was_created(self):
        print(f"Starting _check_if_file_was_created")
        print("platform: ", platform.node())
        if os.path.exists(self.file_to_wait_for):
            self.file_found = True
            print(f"File found-{self.file_to_wait_for}")
            os.remove(self.file_to_wait_for)
        else:
            self.file_found = False
            print(f"File not found-{self.file_to_wait_for}")
        
        print(f"Stopping _check_if_file_was_created")
            
            
    async def run(self):
        print(f"Starting run")
        print("platform: ", platform.node())
        while not self.file_found:
            self._check_if_file_was_created()
            print(f"self.file_found: {self.file_found}")
            await asyncio.sleep(1)
        yield TriggerEvent(self.file_to_wait_for)

    def serialize(self) -> Tuple[str, Dict[str, Any]]:
        print(f"Starting serialize")
        print("platform: ", platform.node())
        return ("spark_job_data_consumer.SuccessFileTrigger", {"file_input_directory": self.file_input_directory})

class SparkSuccessFileSensor(BaseSensorOperator):

    template_fields = ['file_input_directory']

    def __init__(self, file_input_directory: str, **kwargs):
        print("Starting SparkSuccessFileSensor: __init__")
        print("platform: ", platform.node())
        super().__init__(**kwargs)
        self.file_input_directory = file_input_directory
        print("Stopping SparkSuccessFileSensor: __init__")

    def execute(self, context) -> Any:
        print("Starting SparkSuccessFileSensor: execute")
        print("platform: ", platform.node())
        
        self.defer(trigger=SuccessFileTrigger(self.file_input_directory), method_name='mark_sensor_as_completed')
		
        print("Stopping SparkSuccessFileSensor: execute")

    def mark_sensor_as_completed(self, context, event: str):
        print("Starting SparkSuccessFileSensor: mark_sensor_as_completed")
        print("platform: ", platform.node())
            # event is the payload send by the trigger when it yields the TriggerEvent
        return event

def get_date() -> str:
    print("Starting get_date")
    print("platform: ", platform.node())
    
    return str(datetime.now())
  
with DAG(dag_id="spark_job_data_consumer", schedule='@daily', start_date=datetime(2023, 9, 27)) as spark_job_data_consumer:
    success_file_sensor = SparkSuccessFileSensor(
        task_id='success_file_sensor',
        file_input_directory='/tmp/spark_job_data/{{ ds_nodash }}',
    )



    task_get_date = PythonOperator(
        task_id='get_date',
        python_callable=get_date,
        do_xcom_push=True
    )
    
    success_file_sensor >> task_get_date
