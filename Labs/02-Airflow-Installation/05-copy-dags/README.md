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
ls
```

## Copy to local Airflow installation
```
sudo rm -rf /airflow-2/dags/$USER
```

```
sudo mkdir -p /airflow-2/dags/$USER
cd ~/apache-airflow-sep-23/Labs/Airflow-Dags-Hands-on
sudo cp -r . /airflow-2/dags/$USER
tree /airflow-2/dags/$USER
```


## Copy to GCP Composer
```
rm -rf ~/mnt/composer/dags/$USER
```

```
mkdir -p ~/mnt/composer/dags/$USER
cd ~/apache-airflow-sep-23/Labs/Airflow-Dags-Hands-on
cp -r . ~/mnt/composer/dags/$USER
tree ~/mnt/composer/dags/$USER
```

