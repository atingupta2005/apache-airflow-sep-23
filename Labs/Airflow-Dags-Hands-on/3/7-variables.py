from datetime import datetime
from airflow.models import DAG, Variable
from airflow.operators.python import PythonOperator


def print_variables() -> str:
    var_user_email = Variable.get("user_email")
    var_sample_json = Variable.get("sample_json", deserialize_json=True)
    var_env_test = Variable.get("test")
    var_env_test_json = Variable.get("test_json", deserialize_json=True)

    return f"""
        var_user_email = {var_user_email},
        var_sample_json = {var_sample_json},
        var_env_test = {var_env_test},
        var_env_test_json = {var_env_test_json}
    """


with DAG(
    dag_id="7-variables",
    schedule_interval="@daily",
    start_date=datetime(2022, 3, 1),
    catchup=False
) as dag:
    task_print_variables = PythonOperator(
        task_id="print_variables",
        python_callable=print_variables
    )