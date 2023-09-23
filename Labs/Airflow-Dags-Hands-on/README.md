# Setup all the dags in Composer
## Make sure that we have mounted the DAGs folder
## Run below commands to copy the DAG files with your dag id suffix in the DAG folder
```
cd ~
git clone https://github.com/atingupta2005/apache-airflow-sep-23
```

```
cd ~/apache-airflow-sep-23/Labs/Airflow-Dags-Hands-on
```

```
chmod a+x updates-files.sh
. ./updates-files.sh
```

```
ls 1
ls 2
cat 1/$USER-1-00_umbrella.py
cat 2/$USER-2-01_start.py
```


```
rm -rf ~/mnt/composer/dags/$USER
mkdir -p ~/mnt/composer/dags/$USER
```

```
cp -r . ~/mnt/composer/dags/$USER
```

```
ls ~/mnt/composer/dags
```
