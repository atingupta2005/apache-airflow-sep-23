# Use Dockerfile to setup Airflow
```
cd ~
git clone https://github.com/atingupta2005/apache-airflow-sep-23
cd apache-airflow-sep-23
```

```
cd ~/apache-airflow-sep-23/Labs/02-Airflow-Installation/04-Install-using-Docker-airflow-v2
sudo mkdir /airflow-2
sudo chmod 777 /airflow-2
cd /airflow-2
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
cd -
cp *.sh docker-compose.yaml /airflow-2/
cd /airflow-2
chmod a+x ./start.sh
docker compose --profile flower up -d
```

