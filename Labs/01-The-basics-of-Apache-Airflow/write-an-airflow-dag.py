from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
'owner': 'airflow',
' start_date ': airflow.utils.dates.days_ago (2),
' depends_on_past ': False,
'email': ['airflow@example.com'],
' email_on_failure ': False,
' email_on_retry ': False,
# If a task fails, retry it once after waiting at least 5 minutes
'retries': 1,
' retry_delay ': timedelta (minutes=5),
}

dag = DAG(
'dag -sample',
default_args = default_args ,
description='A simple tutorial DAG',
# Continue to run DAG once per day
schedule_interval = timedelta (days=1),
)


  # t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator ( task_id =' print_date ’, bash_command ='date’, dag = dag ,)
t2 = BashOperator ( task_id ='sleep’, depends_on_past =False, bash_command ='sleep 5', dag = dag ,)
templated_command = """
{% for i in range(5) %}
echo "{{ ds }}"
echo "{{ macros.ds_add (ds, 7)}}"
echo "{{ params.my_param }}"
{% endfor %}
"""
t3 = BashOperator ( task_id ='templated', depends_on_past =False, bash_command = templated_command , params={' my_param ': 'Parameter I passed in'}, dag = dag ,)


t1 >> t2
t2 << t1
t1.set_downstream([t2, t3])
t1 >> [t2, t3]
[t2, t3] << t1
# t2 will depend on t1
t1.set_downstream(t2)
# t3 will depend on t1
t3.set_upstream(t1)