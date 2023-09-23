# Installing Airflow with Rancher and Kubernetes Executor
- Rancher has feature of Catalog which is a collection of Helm charts
- We will deploy Airflow using Catalog
- Click on Apps -> Manage Catalogs
- Click Add Catalog
  - Name: airflow charts
  - Catalog URL: http://github.com/atingupta2005/airflow-helm-chart.git
- Click Create
- Click Apps again and click Launch
- Select Airflow-K8s catalog
- Configure the Chart and install
  - Name: airflow
  - Template Version: 4.4.0
  - Target Project: Default
  - Available Roles: Cluster
- Click Launch
- Wait for 5- 10 min and then check if Airflow is running
- Browse through Rancher to inspect the components deployed
- Connect to the shell of webserver pod
```
ls
ls dags
```
