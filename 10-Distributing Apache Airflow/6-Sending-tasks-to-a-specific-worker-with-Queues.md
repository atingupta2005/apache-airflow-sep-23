# Sending tasks to a specific worker with Queues
- When we use the Celery executer we can specify the queue where we want to send some of the tasks of a given DAG
- For example if we have a CPU intensive task and one worker node has more CPUs than the others
- Another example - a task interacting with Spark and only one of the worker node has Spark installed on new cluster
- Basically you can specialize your worker either from a resource perspective or from an environment perspective
- To use the queue we need to do below 2 things:
  - When we create a new worker with the command - "airflow worker", we have to add the option -q with the name of the queue so that the worker will only pick up tasks wired to that spcified queue.  We can add multiple queues by separating them with commas
  ```
  airflow worker -q queue_1, queue_2
  ```
  - The last thing to do is to set the attribute "queue" of the tasks we want to send. All operators have an attribute called queue. By default it is set to default
    - airflow.cfg -> default_queue = default

## Add a worker to read from a specific queue
- Open file - docker-compose-CeleryExecutor.yml
  - In the service - worker, from the command instruction, after "worker" add -q worker_ssd, worker_cpu, worker_spark
    - Here we going to create 3 queues - worker_ssd, worker_cpu and worker_spark
    - If there are 3 workers then each worker will be assigned to a specific queue

- Start Airflow
```
docker ps
docker-compose -f docker-compose-CeleryExecutor.yml up -d --scale worker=3
docker ps
```
- Open flower dashboard
- There are 3 workers
- If we open any of the worker -> Queues tab, notice that tjis worker is assigned to 3 queues
- Open Airflow UI
- Enable queue_dag and refresh the page until DAG runs
- Open flower dashboard
- Notice no tasks are running as all tasks are by default assigned to the queue - default
- Since queue doesn't exist anymore, there is no way for the workers to pull the tasks neither for the scheduler to send them
- How to fix?
- Open terminal and stop Airflow UI
```
docker-compose -f docker-compose-CeleryExecutor.yml down
```
- Change docker-compose-CeleryExecutor.yml and specify  -q worker_ssd, worker_cpu, worker_spark, default
- Change the DAG - queue_dag.py
  - add the queue arguement to the task operator - queue = '<queue-name>'
- Start Airflow UI
```
docker ps
docker-compose -f docker-compose-CeleryExecutor.yml up -d --scale worker=3
docker ps
```
- Currently all the workers are accepting the tasks from all the queues. Each worker should only accept tasks either from default queue or from the queue having the tasks for that specific worker.
- Open flower dashboard and open each worker one by one and then remove the queue from each
- Open Airflow UI and turn on the dag - queue_dag
- Refresh until first task runs
- Open flower dashboard
- We can see that worker_1 has executed 3 tasks which are the higher 3 tasks from the DAG.
- Actually we can check this by clicking on "Tasks"
- In search box specify - _ssd and notice that only worker_1 has executed ssd specific tasks
- In search box specify - _cpu and notice that only worker_2 has executed CPU intensive tasks
- In search box specify - _spark and notice that only worker_3 has executed this task
- So everything is as expected
- In search box specify - task_7 and notice which worker has executed it
- Stop the Aurflow cluster
```
docker-compose -f docker-compose-CeleryExecutor.yml down
```
