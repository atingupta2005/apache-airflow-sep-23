# Mastering DAGs

# The most important parameters

## Downstream and upstream
![](img/downstream-upstream.png)


* start_date
  * The date from which tasks of your DAG can be scheduled and triggered.
* schedule_interval
  * The interval of time from the min(start_date) at which your DAG should be triggered.
* The DAG \[X\] starts being scheduled from the start_date and will be triggered after every schedule_interval

# What is the execution_date

![](img/9-Mastering%20DAGs1.png)

# Execution flow

![](img/9-Mastering%20DAGs2.png)

# How to define the scheduling_interval

* Either with
  * Cron expressions (ex: 0 \* \* \* \*)
  * Timedelta objects (ex: datetime .timedelta(days=l ))
* As a best practice you should use cron expressions rather than timedelta objects as specified in the documentation.

# What about end_date?

The date at which your DAG/Task should stop being scheduled

Set to None by default

Same recommendations than start_date

# Backfill and Catchup

Kick off the missing DAG runs

# DagRun

The scheduler creates a DagRunobject

Describes an instance of a given DAG in time

Contains tasks to execute

Atomic, Idempotent

![](img/9-Mastering%20DAGs3.png)

# Dealing with timezones in Airflow

Make your DAGs timezone dependent

# Definition

* A timezone is a region of the globe that observes a uniform standard time
* Most of the timezones on land are offset from Coordinated Universal Time (UTC)
* Example:
  * Paris: UTC+2:OO
  * Newyork: UTC-4:OO

# Timezone in Python: Naive vs Aware

* Python datetime.datetimeobjects with the tzinfo attribute set
  * Datetime aware
* Python datetime.datetimeobjects without the tzinfo attribute set
  * Datetime naive
* Why it matters?
  * Interpretation of naive datetime objects: BAD

# Best Practices!

* ALWAYS USE AWARE DATETIME OBJECTS
  * datetime.datetime() in python gives naive datetime objects by default
  * A datetime without a timezone is not in UTC
  * Import airflow.timezone to create your aware datetime objects
  * Or let Airflow does the conversion for you

# Timezones in Airflow

* Airflow supports timezones
* Datetime information stored in UTC
* User interface always shows in datetime in UTC
* Up to the developer to deal with the datetime
* The timezone is set in airflow.cfg to UTC by default
  * default_timezone=utc
* Airflow uses the pendulum python library to deal with time zones

# How to make your DAG timezone aware?

* Supply a timezone aware start_date using Pendulum:
  * <span style="color:#0070C0">import pendulum</span>
  * <span style="color:#0070C0">local_tz</span>  <span style="color:#0070C0">=</span>  <span style="color:#0070C0">pendulum.timezone</span>  <span style="color:#0070C0">(“Europe/Amsterdam”)</span>
  * <span style="color:#0070C0">default_args</span>  <span style="color:#0070C0">= \{ ‘</span>  <span style="color:#0070C0">start_date</span>  <span style="color:#0070C0">’: datetime(2019, 1, 1,</span>  <span style="color:#0070C0">tzinfo</span>  <span style="color:#0070C0">=</span>  <span style="color:#0070C0">local_tz</span>  <span style="color:#0070C0">), owner=’Airflow’ \}</span>
  * <span style="color:#0070C0">with DAG(‘</span>  <span style="color:#0070C0">my_dag</span>  <span style="color:#0070C0">',</span>  <span style="color:#0070C0">default_args</span>  <span style="color:#0070C0">=</span>  <span style="color:#0070C0">default_args</span>  <span style="color:#0070C0">):</span>
    * <span style="color:#0070C0">…..</span>

# How to make your tasks dependent

depends_on_past and wait_for_downstream

# depends_on_past

Defined at task level

If previous task instance failed, the current task is not executed

Consequently, the current task has no status

First task instance with start_date allowed to run

![](img/9-Mastering%20DAGs7.png)

# wait_for_downstream

Defined at task level

An instance of task X will wait for tasks downstream of the previous instance of task X to finish successfully before it runs.

Runs concurrently

![](img/9-Mastering%20DAGs8.png)

Doesn't start because downstream tasks are not finished in DAGRUN 2

waiLfor_downstream=true

![](img/9-Mastering%20DAGs9.png)

# How to structure your DAG folder

Managing your files and DAGs

# DAG Folder

Folder where your Airflowdagsare

Defined with the parameterdags_folder

The path must be absolute

By default: $AIRFLOW_HOME/dags

Problem: too many DAGs, DAGs using many external files, …

How can we structure the DAG folder?

# First way: Zip

Create a zip file packing your DAGs

The DAGs must be in the root of the zip file

Airflow will scan and load the zip file for DAGs

![](img/9-Mastering%20DAGs10.png)

# Second way: DagBag

* A DagBag is a collection of DAGs, parsed out of a folder tree and has a high-level configuration settings.
* Make easier to run distinct environments (dev/staging/prod)
* One system can run multiple independent settings set
* Allow to add new DAG folders by creating a script in the default DAGs folder

# .airflowignore

Specifies the directories or files in the DAGs folder that Airflow should ignore

Equivalent to the .gitignorefile

Each line corresponds to a regular expression pattern

The scope of a .airflowignore is the current directory as well as its subfolders

You can avoid wasting scans by using the .airflowignorefile

As best practice, always put a .airflowignorefile in your DAGs folder

# How to deal with failures in your DAGs

# Dag failure detections

* Detection on DAGs
  * DAG level
    * dagrun_timeout
    * sla_miss_callback
    * on_failure_callback
    * on_success_callback

# Dag failure detections

* Detection on DAGs
  * DAG level
    * dagrun_timeout
    * sla_miss_callback
    * on_failure_callback
    * on_success_callback

# Task failures detection

* Detection on Tasks
* Task level
  * email
  * email_on_failure
  * email_on_retry
  * retries
  * retry_delay
  * retry_exponential_backoff
  * max_retry_delay
  * execution_timeout
  * on_failure_callback
  * on_success_callback
  * on_retrv_callback

