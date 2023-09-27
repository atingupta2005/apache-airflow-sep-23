# Templating tasks
- Refer template_dag.py
- Only some parameters are templated in Operators
- Have a look at documentation to understand which parameters can be templated
- Refer to the task t0. Notice the templating using in the Operator. ds is predefined variable

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
