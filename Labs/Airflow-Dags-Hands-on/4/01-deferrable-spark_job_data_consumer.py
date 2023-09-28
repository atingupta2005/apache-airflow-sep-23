import asyncio
from concurrent.futures import ThreadPoolExecutor
from airflow.sensors.base import BaseSensorOperator
from airflow.models.baseoperator import BaseOperator
import os
from pendulum import datetime
from airflow.decorators import dag, task
from airflow.triggers.base import BaseTrigger, TriggerEvent
from typing import Any
from typing import Dict, Tuple
from airflow import DAG


class SuccessFileTrigger(BaseTrigger):
    def __init__(self, file_input_directory: str):
        super().__init__()
        self.file_found = False
        self.file_input_directory = file_input_directory
        self.file_to_wait_for = f'{file_input_directory}/_SUCCESS'

    def _check_if_file_was_created(self):
        logging.info(f'Checking if {self.file_to_wait_for} exists...')
        if os.path.exists(self.file_to_wait_for):
            logging.info('...found file')
            self.file_found = True
        else:
            logging.info('...not yet')

    async def run(self):
        while not self.file_found:
            self._check_if_file_was_created()
            await asyncio.sleep(5)
        yield TriggerEvent(self.file_to_wait_for)

    def serialize(self) -> Tuple[str, Dict[str, Any]]:
        return ("04_deferrable_operators.SuccessFileTrigger", {"file_input_directory": self.file_input_directory})

class SparkSuccessFileSensor(BaseSensorOperator):

    template_fields = ['file_input_directory']

    def __init__(self, file_input_directory: str, **kwargs):
        super().__init__(**kwargs)
        self.file_input_directory = file_input_directory

    def execute(self, context) -> Any:
        self.defer(trigger=SuccessFileTrigger(self.file_input_directory), method_name='mark_sensor_as_completed')

    def mark_sensor_as_completed(self, context, event: str):
            # event is the payload send by the trigger when it yields the TriggerEvent
        return event

with DAG(dag_id="01-deferrable-spark_job_data_consumer", schedule='@daily', start_date=datetime(2022, 11, 15)) as spark_job_data_consumer:
    success_file_sensor = SparkSuccessFileSensor(
        task_id='success_file_sensor',
        file_input_directory='/tmp/spark_job_data/{{ ds_nodash }}',
    )

