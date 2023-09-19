# Templating tasks
- Refer template_dag.py
- Only some parameters are templated in Operators
- Have a look at documentation to understand which parameters can be templated - airflow.readthedocs.io
- Refer to the task t0. Notice the templating using in the Operator. ds is predefined variable
- Start Airflow
```
docker-compose -f docker-compose-CeleryExecutor.yml up -d
docker ps
```
- Open Airflow UI
- Enable template_dag
- Trigger DAG
- Refresh the page
- Open DAG -> Graph View
- Open task t0 and view the logs
- Notice that date is printed in the logs

## Create variable
- Open Airflow UI -> Admin -> Variables
- Create variable named - CASSANDRA_LOGIN
- Open template_dag.py and specify new variable name - var.value.CASSANDRA_LOGIN instead of ds
- Run DAG again and notice that value is printed in the logs

## Use macro
- Update dag code
```
macros.ds_format(ts_nodash, '%Y%m%dT%H%M%S', '%Y-%m-%d-%H-%M')
```
- Trigger DAG again
- View the logs

## Templating the files
- Uncomment t1
- Notice t1 code
- t1 will execute the script - generate_new_logs.sh in order to generate fake logs in the file called logs.csv which you can find from the parameter params. This parameter is a reference to the user-defined params dictionary defined in the calling task.
- It is available for all operators and we can access it from a task either by using template or the context of that task
- Open generate_new_logs.sh and search for params.filename which will be replaced by the value logs.csv at runtime
- Also notice DEST_PATH. The values are templated directly in the file.
  - var.value.source_path - to spcify the path where the log files will be generated
- We need to create the variable - source_path using Airflow UI
  - Value: /usr/local/airflow/dags
- Open template_dag  and enable
- Trigger the DAG
- Refresh the page
- Notice that a new folder named data in created in the folder dags. the folder data has the generated log file
- Open log file and notice the content
- Open Airflow UI and select the last task
- Click Rendered Template
- Notice that in the code the template values are replaced with real values


##
- Open template_dag and uncomment the code for TEMPLATED_LOG_DIR and task t2 which check if the log file has been generated
- Uncomment the task t3 which do some modifications on the logs
- Uncomment dependencies in the last
- Notice task t3
  - provider_context
    - When set to True allow Airflow to pass a set of keyword arguments that can be used in your function
    - Its a way to obtain information about DAG, tasks and so on
    - Exactly as we do with templates using predefined variables - ds, ti and so on
    - This parameter is actually set to True by default so you don't need to specify it anymore
  - template_dict
    - A dictionary where the values will get templated by the Jinja engine and are made available in the context provided
- Set provider_context = True
- Set template_dict = {'log_dir': TEMPLATED_LOG_DIR}
- Open process_logs.py and notice 2 lines
  - log_dir = ...
  - filename = ....
- Open Airflow UI and trigger template_dag
- Refresh the page
- Open code editor and notice a new file is created next to the file - logs.csv
- Notice that parameter params does not accept the templated value so we should not put a placeholder with curly brackets as would not work
- Comment the code before restarting Docker Container
  - Comment task t2
  - Comment task t3
  - Comment task dependencies
  - Comment TEMPLATED_LOG_DIR
- Stop Airflow
```
docker-compose -f docker-compose-CeleryExecutor.yml down
docker ps
```
