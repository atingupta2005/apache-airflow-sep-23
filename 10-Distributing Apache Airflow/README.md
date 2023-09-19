# Distributing Apache Airflow

# Introduction

# An Overview

Sequential Executor with SQLite

Local Executor with Postgres

Set up a cluster with Celery Executor and Docker

Distributing your tasks with the Celery Executor

How to specialize your workers

How to limit task executions with Pools

Scaling Airflow with Kubernetes Executors

Set up a 3 nodes cluster with Kubernetes\, Rancher and Vagrant

And more …\.\.

# Sequential Executor with SQLite

The most basic settings

# What is SQLite?

Relational Database

Not a client\-server\, embedded into the end program ACID compliant

Implement most of the SQL Standard

Almost no configuration to run

Unlimited number of readers

Only one writer at any instant in time

Limited in size up to 140 TB

Database stored into a single disk file

# How a task gets executed?

When a DAG is scheduled\, each task has a record with its status \(queued\, scheduled\, running\, success\, failed\) stored into the metadata database\.

The Scheduler periodically reads from the metadata database to check if there is any task to run\.

The Executor gets the tasks to run from its internal queue and specify how to execute it \(Sequential\, Local\, Celery\, K8s\)

# What is the Sequential Executor?

Most basic executor

Only run one task at a time

Only executor to use with SQLite

Default configuration

Should not be used in production\, only for debugging purposes in the context of Airflow

# Parameters

* Inairfiow\.cfg
  * executor=SequentialExecutor
  * sql\_alchemy\_conn=sqlite:////home/airflow/airflow/airflow\.db

# Local Executor with PostgreSQL

# What is the Local Executor?

Run multiple tasks in parallel

Base on the python module: multiprocessing Spawn processes to execute tasks

Easy to set up

Resource light

Vertical Scaling

Single point of failure

As a best practice\, always try the Local Executor first\! KISS \(Keep it simple\, stupid\)

# What is PostgreSQL?

Object relational database

ACID compliant

Client\-server database

Handle concurrent connections

SQL standard and advanced

Highly scalable

Extensible

# Concurrency and parallelism parameters

![](img/10-Distributing%20Apache%20Airflow1.png)

# Local Executor strategies

* parallelism = 0
  * "Unlimited" parallelism
* parallelism > 0
  * Limited parallelism
* As a best practice\, set parallelism to:
  * number\_of\_cores\- 1

# Scale out Apache Airflow with Celery Executors

Distributed mode

# What is the Celery Executor?

Scale out Apache Airflow

Backed by Celery: Asynchronous Distributed Task Queue

Distribute tasks among worker nodes

airflow worker: Create a worker to execute tasks

Horizontal Scaling

High availability: If one worker goes down\, Airflow can still schedule tasks

Need a message broker: RabbitMQ/Redis

Can set different queues

![](img/10-Distributing%20Apache%20Airflow2.png)

# What are the drawbacks?

Need an extra component: Message Broker Service

Take time and work to set up

Worker maintenance

# Reminder about Kubernetes

Before using the Kubernetes executors

# Kubernetes is extremely powerful

* Open source project founded by Google in 2014\.
* Container orchestrator
* Kubernetes automates sysadmin tasks:
  * Upgrading servers\, installing security patches\, configuringneworks\, running backups\, failover\, monitoring
* Zero\-downtime deployments with rolling updates
* Provides facilities to implement CD practices: Canary / Blue\-green
* Supports autoscaling \(up and down\)
* Redundancy and failover built in\, applications more reliable and resilient
* And more\.\.\.

# … but has some gotchas

Setting up correctly a K83 is a real pain\.

Hard to maintain\.

The learning curve is steep\.

# Cluster Architecture

![](img/10-Distributing%20Apache%20Airflow3.png)

# Important Kubernetes objects

![](img/10-Distributing%20Apache%20Airflow4.png)

* Pod
  * Group of one or more containers
* Replica Set
  * Ensures that a specified number of pod replicas are running at any given time\.
* Service
  * Defines a logical set of Pods and a policy by which to access them\.
* Storage class
  * Provides a way to describe a "class” of storage\. Represents a Persistent Volume\.
* Persistent Volume Claim
  * Abstraction of Persistent Volumes\. A Persistent volume is a piece of storage in the cluster

# Scaling Airflow with Kubernetes Executors

The next level

# Drawbacks of the Celery Executor

Need to set up tier applications \(RabbitMQ\, Celery\, Flower\)

Deal with missing dependencies

Wasting resources: airflow workers stay idle when no workload

Worker nodes are not as resilient as you think

Nonetheless\, it stays a widely used executor in production

# What is the Kubernetes Executor?

* Runs your tasks on Kubernetes
* One task = One Pod
* Task\-level Pod configuration
* Expands and shrinks your cluster according to the workload
* Pods run to completion
* Scheduler subscribes to Kubernetes event stream
* DAG distribution
  * Git clone withinit\-container for each Pod
  * Mount volume with DAGs
  * Build image with the DAG codes

Git clone withinit\-container for each Pod

![](img/10-Distributing%20Apache%20Airflow5.png)

Cl/CD pipeline with Airflow image containing DAGs

![](img/10-Distributing%20Apache%20Airflow6.png)

# What are the drawbacks?

Kubernetes is hard

Still new

# What is the Kubernetes Executor?

![](img/10-Distributing%20Apache%20Airflow7.png)
