# Use Dockerfile to setup Airflow
```
git clone https://github.com/atingupta2005/apache-airflow-sep-23
cd apache-airflow
```

```
cd ~/apache-airflow-sep-23/Labs/02-Airflow-Installation/03-Install-using-Docker
docker build -t airflow-basic .
docker images
```

```
docker run -d --name airflow_1 -v ~/dags:/opt/airflow/dags  -p 8080:8080 airflow-basic
```
