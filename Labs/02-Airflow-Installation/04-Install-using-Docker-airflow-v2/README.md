# Use Dockerfile to setup Airflow
```
cd ~
rm -rf apache-airflow-sep-23
git clone https://github.com/atingupta2005/apache-airflow-sep-23
cd apache-airflow-sep-23
```

```
cd ~/apache-airflow-sep-23/Labs/02-Airflow-Installation/04-Install-using-Docker-airflow-v2
sudo chmod -R 777 /airflow-2
```

```
echo -e "AIRFLOW_UID=$(id -u)" > /airflow-2/.env
ls *.sh
```

```
cp *.sh docker-compose.yaml /airflow-2/
cd /airflow-2
sudo chmod -R 777 /airflow-2
```

```
ls
chmod a+x ./*.sh
mkdir -p /airflow-2/config/dags
mkdir -p /airflow-2/config/plugins
mkdir -p /airflow-2/config/logs
ls
```

```
docker compose --profile flower up -d
ls
```

