# Clean up the Composer database
- As the time goes, the Airflow database of your environment stores more and more data. This data includes information and logs related to past DAG runs, tasks, and other Airflow operations.

- Make sure to run the maintenance DAG periodically to keep the database size below 16 GB. It is recommended to run this DAG daily for most environments. 
If you observe that database size metric increases significantly between runs, consider running this DAG more often.

- Choose a retention period (DEFAULT_MAX_DB_ENTRY_AGE_IN_DAYS) that allows keeping database below 16 GB. Recommend a period of 30 days as a starting point for most environments.

- This DAG removes old entries from job, dag_run, task_instance, log, xcom, sla_miss, dags, task_reschedule, task_fail and import_error tables by default. In the DAG, review the list of tables and decide whether old entries must be removed from them. In general, most space savings are provided by cleaning log, task_instance, dag_run and xcom tables. To exclude a table from cleanup, modify the DAG and comment corresponding items in the DATABASE_OBJECTS list.
