### Reference
 - https://github.com/kaxil/airflowctl#installation

```
cd ~
```

```
sudo apt install python3-pip -y
```

```
sudo apt install python3.10-venv
```

```
python3 -m venv airflowvenv
```

```
source airflowvenv/bin/activate
```


```
pip install airflowctl
```

```
airflowctl init ag_airflow_project --build-start &
```

```
airflowctl list
```

```
airflowctl stop ag_airflow_project
```

```
airflowctl start ag_airflow_project
```

```
airflowctl info
```

```
airflowctl info ag_airflow_project
```

```
airflowctl airflow version
```

```
airflowctl airflow dags list
```