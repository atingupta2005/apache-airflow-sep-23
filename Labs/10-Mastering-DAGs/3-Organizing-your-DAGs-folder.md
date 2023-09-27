# Organizing your DAGs folder
## DagBag
```
docker ps
docker logs -f <container-id>
```

- Check the logs - "Filling Up the DagBag" - every 30 seconds
- Can change the interval from airflow.cfg

```
./stop.sh
```

- Edit add_dagbags.py
- It has the paths of DagBags
- Uncomment and save it
- Copy backfill.py to 2 folders - project_a and project_b
- Rename the file name copied in project_a and project_a to project_a.py and project_b.py
- Change the DAG id in the py files
- Save files
```
./start.sh
```
- Open airflow UI
- Notice that both the DAGs are now available
- Note that there must be no errors in our DAG files, else they will not be shown on UI
- Now if we make an error on one of the DAGs then that DAG will not be available
