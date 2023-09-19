# Running DAGs with Kubernetes Executor
- We will see what happens when tasks of a DAG are run through the Kubernetes Executor
- Open rancher dashboard. Open Resources -> Airflow
- We should have Airflow running. The webserver, scheduler and the database pods should be shown as running on Rancher Dashboard
- We need to access the PODs out of cluster using services. Service is used for enabling network access to the POD
- Refer to Service Discovery tab to inspect the existing services
- Notice the private IP address of the service
- Since this is the private ip address, we can't access it from our web browser
- We need to enable Port Forwarding for the same.
- Open Apps -> Airflow app -> Notes
- Refer to the instructions to access Airflow from web browser
- Open session to master node and execute these instructions
  - Open terminal
  ```
  vagrant ssh master
  ```
  - Copy the code to be executed on the terminal and then execute on terminal
  - To allow all IP addresses to connect, specify -> --address 0.0.0.0
  - Run below commands
  ```
  echo $POD_NAME
  kubectl get pods --all-namespaces
  ```
  - If required, we also need to do port forwarding on VirtualBox
  - Open web browser and open Airflow UI using <master-node-public-ip>:8080
  - Open new terminal and open session to master
  ```
  vagrant ssh master
  ```
- To see what happens when DAG is triggered, run
```
watch kubectl get pods -n <namespace-name-where-pods-created>
```
- Open Airflow UI and enable DAG
- Refer to terminal and notice that 3 more PODs are getting created
- Destroy the cluster
  - disconnect from master
  - destroy all the vagram vms
  ```
  vagrant destroy
  ```
  - Stop docker container
  ```
  docker ps
  docker stop <container-id-of-rancher>
  docker rm <container-id-of-rancher>
  ```
