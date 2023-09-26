from datetime import datetime 
from airflow import DAG 
from airflow.sensors.filesystem import FileSensor 

with DAG(dag_id='16-sensor', start_date=datetime(2023, 1, 1)) as dag: 
    wait_for_file = FileSensor( 
        task_id='wait_for_file', 
        filepath='/tmp/myfile.txt', 
        mode='reschedule', 
        timeout=300, 
        poke_interval=60, 
    ) 
    
    # Define other tasks here 
    print_file_content = BashOperator(
    task_id='print_file_content',
    depends_on_past=False,
    bash_command='cat /tmp/myfile.txt',
    trigger_rule='all_failed',
    dag=dag)

    
    wait_for_file >> print_file_content