```
cd ~
rm -rf apache-airflow-sep-23
git clone https://github.com/atingupta2005/apache-airflow-sep-23
```

```
cd ~/apache-airflow-sep-23/Labs/Airflow-Dags-Hands-on
#git stash
```

```
sudo chmod a+x setup-dags.sh
```

```
. ./setup-dags.sh
```


```
ls 1
cat 1/$USER-1-00_umbrella.py
```

```
sudo rm -rf /airflow-2/dags/$USER
```

```
sudo mkdir -p /airflow-2/dags/$USER
cd ~/apache-airflow-sep-23/Labs/Airflow-Dags-Hands-on
sudo cp -r . /airflow-2/dags/$USER
ls /airflow-2/dags/$USER/1
```
