# Adding new worker nodes with the Celery Executor
- Start existing Airflow cluster
```
docker ps
docker-compose -f docker-compose-CeleryExecutor.yml up -d
docker ps
```
- Create new worker

```
docker network ls
#Note: Replace . with current working directory
docker run --network airflow-section-5_default --expose 8793 -v ./mnt/airflow/dags:/usr/local/airflow/dags -v ./mnt/airflow/airflow.cfg:/usr/local/airflow/airflow.cfg  -dt python:3.7
docker ps
```
- Open localhost:5555
- As we have not connected our new worker to the cluster, it will show only 1 worker in flower dashboard
- Let's connect to the new docker container
```
docker ps
docker exec -it <container id> bash
# export AIRFLOW_HOME=/usr/local/airflow/
# useradd -ms /bin/bash -d $AIRFLOW_HOME airflow
# pipe install "apache-airflow[celery, crypto, postgres, redis]==1.10.6"
# airflow init db
# chown -R airflow: $AIRFLOW_HOME
# su - airflow
$ ls
```
- Open airflow.cfg and change the value of sql_alchemy_conn to specify connection string of postgrss database
```
postgresql+psycopg2://airflow:airflow@postgres:5432/airflow
```
- Set executor = CeleryExecutor
- Set result_backend = db+postgresql://airflow:airflow@postgres:5432/airflow
  - When a job finishes, the Executor needs to update the metadata of the job. Therefore it will insert a message into a database that will be used by the scheduler to update the state of the task
- We had used the same value in environment variable when we defined docker-compose-CeleryExecutor.yml
- If we want to use mysql instead of postgress, we would just need to change all the references of postgress to mysql
- Set broker_url = redis://:redispass@redis:6379/1
- Open terminal add this node to cluster
```
export AIRFLOW_HOME=/usr/local/airflow
airflow worker
```
- Open flower dashboard and notice we have a new worker node
- Open Airflow UI and enable parallel_dag
- Refresh Page
- Open Flower dashboard and notice that both workers are executing tasks
- What happens if any worker node is not available?
```
docker ps
docker kill <id-of-new-container>
```
- Now open flower dashboard
- Notice that one worker node is shown as Offline
- Now what happens when a task is running on a node and that node crashes?
- Click on Tasks and check the tasks by Status - Started
  - It corresponds to the active task in the crashed worker
  - Notice the task name and execution date in args
- Open Airflow UI and click on the DAG
- Find the task with same execution date we notices in args in flower
- Notice that the task is in success state as shown by the square in green
- Open it and check the logs. Notice that this task has not any output that it's succeeded.
- Also this task is never executed by another worker because if any task is running and worker node crashes, we need to rerun the task manually by clearing the task

## Create worker node easily using docker compose
```
docker-compose -f docker-compose-CeleryExecutor.yml scale worker=3
```
- Open flower dashboard and notice that now there are 3 worker nodes
- Stop Airflow
```
docker-compose -f docker-compose-CeleryExecutor.yml down
```
