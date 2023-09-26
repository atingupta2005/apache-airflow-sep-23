# Troubleshooting
## Cleaning up Root Partition Space by Removing the Task Logs
- You can set up a cron to cleanup root partition space filled by task log. Usually Airflow cluster runs for a longer time, so, it can generate piles of logs, which could create issues for the scheduled jobs
```
ls $AIRFLOW_HOME/logs
```

## Using macros with Airflow
- Macros are a set of pre-defined variables and functions that can be used in your DAG definitions. They are useful for dynamic programming and to ensure code reusability.
- Variables and macros can be used in templates

### Default variables
   1. {{ ds }}  - the execution date as YYYY-MM-DD
   2. {{ prev_ds }} - the previous execution date as YYYY-MM-DD
   3. {{ yesterday_ds }} - the day before the execution date as YYYY-MM-DD
   4. {{ ts }} - same as execution_date.isoformat()
   5. {{ execution_date }} - the execution date

```
{{ execution_date.strftime("%Y-%m-%d") 
```

### Macros
```
{{ (execution_date - macros.timedelta(hour=1) }}  # previous hour of current execution date
```

## When a DAG has X number of tasks but it has only Y number of running tasks
- Check the DAG concurrency in airflow configuration file(ariflow.cfg).


## Which logs do I look up for Airflow cluster startup issues?
- Refer to Airflow Services logs which are brought up during the cluster startup.

## Where can I find Airflow Services logs?
$AIRFLOW_HOME/logs/airflow

## What is $AIRFLOW_HOME?
- $AIRFLOW_HOME is a location that contains all configuration files

## Where can I find Airflow Configuration files?
- Configuration file is present at “$AIRFLOW_HOME/airflow.cfg”.


## Where can I find Airflow DAGs?
- The DAGs’ configuration file is available in the $AIRFLOW_HOME/dags folder.

## Where can I find Airflow task logs?
- The task log configuration file is available in $AIRFLOW_HOME/logs

## How do I restart Airflow Services?


## How do I delete a DAG?
- Delete the DAG file using the following command: rm <file_name>
- With the DAG file removed, you can now delete the DAG from the UI

## Tasks are Slow to Schedule or Aren’t Being Scheduled
- If your Scheduler is not doing its job well – or at all – examine and adjust your scheduler parameters; scheduler settings are in the airflow.cfg. file. You have several options:

 - Increase the frequency at which Airflow scans the DAGs directory. Higher frequencies (the default is every 300 seconds) are more CPU-intensive.
 - Increase the frequency at which the Scheduler parses your DAG files. Again, a higher frequency means more CPU usage; consider increasing the value (that is, lowering the frequency).
 - Increase the number of processes the Scheduler can run in parallel.    

## Task Logs are Missing or Fail to Display
- Missing logs typically are due to a failed process in your scheduler or in a worker
- Absent that, try clearing the task instance in the Airflow UI and re-running the task. Other possibilities:
  - Increase the timeout for fetching logs in the log_fetch_timeout_sec file
  - Search for the log file from within a Celery worker
  - Add resources to the workers

#### log_fetch_timeout_sec
- The amount of time (in secs) webserver will wait for initial handshake while fetching logs from other worker machine


## You receive an “unrecognized arguments” error
- This could happen because the DAG file is not being properly imported into the Airflow system, or because there is a problem with the DAG file itself.


## Tasks Run Slow or Fail
- There are many ways tasks can fail to complete, and each scenario has multiple potential causes
### For tasks that aren’t running, it could be because:
 - the task is paused
 - the start date in the past
 - the Scheduler isn’t running properly
 
### For tasks that show as failed, you may be able to pinpoint the issue in the Airflow UI.  Otherwise, check the logs.
 - the task may have run out of memory
 - Airflow automatically shuts down tasks that take too long to execute.  Again, assign more resources to enable faster execution.


## Tasks are Bottlenecked
- Are you running many tasks in parallel. If so, set a higher number of tasks in parallelism.
- Are you scheduling too many tasks to run at one time?  If so, increase the number of DAG runs in max_active_runs_per_dag

- there are more tasks than the environment has the capacity to run

  - Solution: reduce the number of tasks your DAGs run concurrently or increase the number of assigned workers
  



