# Basics of Airflow
# A typical workflow

![](img/1-The%20basics%20of%20Apache%20Airflow1.png)

# Data pipelines

Consist of several tasks

To achieve the desired result

![](img/1-The%20basics%20of%20Apache%20Airflow2.png)

__Overview of the weather dashboard use case\, in which weather data is fetched from an external API and fed into a dynamic dashboard__

# Data pipelines as graphs

![](img/1-The%20basics%20of%20Apache%20Airflow3.png)

Graph representation of the data pipeline for the weather dashboard\.

# DAG

![](img/1-The%20basics%20of%20Apache%20Airflow4.png)

![](img/1-The%20basics%20of%20Apache%20Airflow5.png)

![](img/1-The%20basics%20of%20Apache%20Airflow6.png)

![](img/1-The%20basics%20of%20Apache%20Airflow7.png)

# Airflow DAG

![](img/1-The%20basics%20of%20Apache%20Airflow8.png)

# Airflow

An open source solution for developing and monitoring workflows

![](img/1-The%20basics%20of%20Apache%20Airflow9.png)

Pipelines are defined as DAGs using Python code in DAG files

Each DAG file typically defines one DAG\, which describes the different tasks and their dependencies

Also defines a schedule interval

# Why Airflow?

* Can handle upstream/downstream dependencies gracefully
* Easy to reprocess historical jobs
* Handle errors and failures gracefully
  * Automatically retry when a task fails
* Ease of deployment of workflow changes \(continuous integration\)
* Integrations with a lot of infrastructure
  * Hive\, Presto\, Druid\, AWS\, Google cloud\, etc
* Data sensors to trigger a DAG when data arrives
* Job testing through airflow itself
* Accessibility of log files and other meta\-data through the web GUI
* Monitoring all jobs status in real time \+ Email alerts
* Community support

# Overview of the main components

![](img/1-The%20basics%20of%20Apache%20Airflow10.png)

# Process involved to develop & execute pipelines

![](img/1-The%20basics%20of%20Apache%20Airflow11.png)

# Web Interface of Airflow UI

![](img/1-The%20basics%20of%20Apache%20Airflow12.png)

__The main page of Airflow’s web interface\, showing an overview of the available DAGs and their recent results__

# Airflow applications

Data warehousing

Machine Learning

Email targeting

Data infrastructure maintenance

# Airflow Concepts

# Operators, and Tasks

* DAGs do not perform any actual computation
  * Instead\, __Operators__ determine what actually gets done
* Task
  * Once an operator is instantiated\, it is referred to as a “task”
  * An operator describes a single task in a workflow\.
* A DAG is a container that is used to organize tasks

![](img/1-The%20basics%20of%20Apache%20Airflow13.png)

# Operators categories

* Sensors
  * Will keep running until a certain criteria is met
    * Example include waiting for a certain time\, external file\, or upstream data source\.
* Operators
  * Triggers a certain action
    * e\.g\. run a bash command\, execute a python function\, or execute a Hive query\, etc
* Transfers
  * Moves data from one location to another
    * __MySqlToHiveTransfer__ : Moves data fromMySqlto Hive\.
    * __S3ToRedshiftTransfer__ : load files from s3 to Redshift

# Airflow Tasks

![](img/1-The%20basics%20of%20Apache%20Airflow14.png)

__Overview of the tasks in an individual DAG and the dependencies between these tasks__

# Write an Airflow DAG

# Steps to write an Airflow DAG

Step 1: Importing modules

Step 2: Default Arguments

Step 3: Instantiate a DAG

Step 4: Tasks

Step 5: Setting up Dependencies

# Step 1: Importing modules
```
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
```

# Step 2: Default Arguments
```
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
```

# Step 3: Instantiate a DAG
```
dag = DAG(
'dag -sample',
default_args = default_args ,
description='A simple tutorial DAG',
# Continue to run DAG once per day
schedule_interval = timedelta (days=1),
)
```

# Step 4: Tasks
```
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
```

# Step 5: Setting up Dependencies
```
t1 >> t2
t2 << t1
t1.set_downstream([t2, t3])
t1 >> [t2, t3]
[t2, t3] << t1
# t2 will depend on t1
t1.set_downstream(t2)
# t3 will depend on t1
t3.set_upstream(t1)
```

# DagRuns

* execution\_time
  * Begin at the DAG’sstart\_dateand repeat everyschedule\_interval\.
* For eachexecution\_time\, aDagRunis created and operates under the context of that execution time
* ADagRunis simply a DAG that has a specific execution time\.

# TaskInstances

The task that belongs toDagRuns

# UI DAG Graph View

![](img/1-The%20basics%20of%20Apache%20Airflow15.png)

# UI DAG Tree View

![](img/1-The%20basics%20of%20Apache%20Airflow16.png)

# Incremental loading and backfilling

![](img/1-The%20basics%20of%20Apache%20Airflow17.png)

# Scheduling intervals

![](img/1-The%20basics%20of%20Apache%20Airflow18.png)

![](img/1-The%20basics%20of%20Apache%20Airflow19.png)

__Schedule intervals for a daily scheduled DAG with a specified start date \(2019\-01\-01\)__

__Arrows indicate the time point at which a DAG is executed__

__Without a specified end date\, the DAG will keep being executed every day until the DAG is switched off\.__

* Schedule intervals for a daily scheduled DAG with specified
  * Start \(2019\-01\-01\) and
  * End dates \(2019\-01\-05\)

![](img/1-The%20basics%20of%20Apache%20Airflow20.png)

![](img/1-The%20basics%20of%20Apache%20Airflow21.png)

# Cron-based intervals

* Examples:
  * 0 \* \* \* \* = hourly \(running on the hour\)
  * 0 0 \* \* \* = daily \(running at midnight\)
  * 0 0 \* \* 0 = weekly \(running at midnight on Sunday\)
* More complicated examples:
  * 0 0 1 \* \* = midnight on the first of every month
  * 45 23 \* \* SAT = 23:45 every Saturday

![](img/1-The%20basics%20of%20Apache%20Airflow22.png)

# Airflow presets for frequently

![](img/1-The%20basics%20of%20Apache%20Airflow23.png)

# Frequency-based intervals

![](img/1-The%20basics%20of%20Apache%20Airflow24.png)

__Run every three days following the start date \(on the 4th\, 7th\, 10th\, and so on of January 2019\)\.__

# Execution dates in Airflow

![](img/1-The%20basics%20of%20Apache%20Airflow25.png)

# Execution date

Defined as start time of corresponding schedule interval rather than time at which the DAG is executed \(which is typically the end of the interval\)

As such\, value ofexecution\_datepoints to start of the current interval\, while theprevious\_execution\_dateandnext\_execution\_dateparameters point to start of previous and next schedule intervals\, respectively

Current interval can be derived from a combination of theexecution\_dateand thenext\_execution\_date\, which signifies the start of the next interval and thus the end of the current one\.

![](img/1-The%20basics%20of%20Apache%20Airflow26.png)

# Backfilling

![](img/1-The%20basics%20of%20Apache%20Airflow27.png)

# Best practices for designing tasks

* Atomicity
  * Either all occur or nothing occurs
* Idempotency
  * Rerunning a task without changing the inputs should not change the overall output

# Defining dependencies between tasks

![](img/1-The%20basics%20of%20Apache%20Airflow28.png)

![](img/1-The%20basics%20of%20Apache%20Airflow29.png)

![](img/1-The%20basics%20of%20Apache%20Airflow30.png)


## Installing Airflow manually
- Create and start a docker container from the Docker image python:3.8-slim and execute the command /bin/bash in order to have a shell session
```
docker run -itd -p 8080:8080 --name airflow-basic1 python:3.8-slim /bin/bash
docker ps
docker exec -it airflow-basic1 bash
```


- Print the Python version
```
python -V
```

- Export the environment variable AIRFLOW_HOME used by Airflow to store the dags folder, logs folder and configuration file
```
export AIRFLOW_HOME=/usr/local/airflow
```


- To check that the environment variable has been well exported
```
env | grep airflow
```


- Install all tools and dependencies that can be required by Airflow
```
apt-get update -y && apt-get install -y wget libczmq-dev curl libssl-dev git inetutils-telnet bind9utils freetds-dev libkrb5-dev libsasl2-dev libffi-dev libpq-dev freetds-bin build-essential default-libmysqlclient-dev apt-utils rsync zip unzip gcc && apt-get clean
```


- Create the user airflow, set its home directory to the value of AIRFLOW_HOME and log into it
```
useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow
```


- Show the file /etc/passwd to check that the airflow user has been created
```
cat /etc/passwd | grep airflow
```

- Upgrade pip (already installed since we use the Docker image python 3.5)
```
pip install --upgrade pip
```


- Log into airflow
```
su - airflow
```


- Create the virtual env named sandbox
```
python -m venv .sandbox
```


- Activate the virtual environment sandbox
```
source .sandbox/bin/activate
```


- Download the requirement file to install the right version of Airflow’s dependencies
```
wget https://raw.githubusercontent.com/apache/airflow/constraints-2.0.2/constraints-3.8.txt
```


- Install the version 2.0.2 of apache-airflow with all subpackages defined between square brackets
```
pip install "apache-airflow[crypto,celery,postgres,cncf.kubernetes,docker]"==2.0.2 --constraint ./constraints-3.8.txt
```

- Initialise the metadatabase
```
airflow db init
```


- Start Airflow’s scheduler in background
```
airflow scheduler &
```


- Start Airflow’s webserver in background
```
airflow webserver &
```

- Open in browser
```
curl localhost:8080
```

- Exit from container
```
exit
```

- Delete docker container
```
docker ps
docker container stop airflow-basic1
docker container rm  airflow-basic1
docker ps
```

## Use Dockerfile to setup Airflow
- Clone git repo
```
git clone https://github.com/atingupta2005/apache-airflow
cd apache-airflow
```

- Build a docker image from the Dockerfile in the current directory (airflow-materials/airflow-basic)  and name it airflow-basic
```
cd ~/apache-airflow/01-The\ basics\ of\ Apache\ Airflow/
docker build -t airflow-basic .
docker images
```

```
docker run -d --name airflow_1  -p 8080:8080 airflow-basic
```


## Quick Tour of Airflow CLI
- Show running docker containers
```
docker ps
```

- Execute the command /bin/bash in the container_id to get a shell session
```
docker exec -it airflow_1 /bin/bash
```

- Print the current path where you are
```
pwd
```


- Initialise the metadatabase
```
airflow db init
```


- Reinitialize the metadatabase (Drop everything)
```
airflow db reset
```


- Upgrade the metadatabase (Latest schemas, values, ...)
```
airflow db upgrade
```


- Start Airflow’s webserver
```
airflow webserver &
```


- Start Airflow’s scheduler
```
airflow scheduler &
```


- Start a Celery worker (Useful in distributed mode to spread tasks among nodes - machines)
```
airflow celery worker
```


- Give the list of known dags (either those in the examples folder or in dags folder)
```
airflow dags list
```


- Trigger the dag example_python_operator with the current date as execution date
```
airflow dags trigger example_python_operator
```


- Trigger the dag example_python_operator with a date in the past as execution date (This won’t trigger the tasks of that dag unless you set the option catchup=True in the DAG definition)
```
airflow dags trigger example_python_operator -e 2021-01-01
```


- Trigger the dag example_python_operator with a date in the future (change the date here with one having +2 minutes later than the current date displayed in the Airflow UI). The dag will be scheduled at that date.
```
airflow dags trigger example_python_operator -e '2021-01-01 19:04:00+00:00'
```


- Display the history of example_python_operator’s dag runs
```
airflow dags list-runs -d example_python_operator
```


- List the tasks contained into the example_python_operator dag
```
airflow tasks list example_python_operator
```


- Allow to test a task (print_the_context) from a given dag (example_python_operator here) without taking care of dependencies and past runs. Useful for debugging.
```
airflow tasks test example_python_operator print_the_context 2021-01-01
```
