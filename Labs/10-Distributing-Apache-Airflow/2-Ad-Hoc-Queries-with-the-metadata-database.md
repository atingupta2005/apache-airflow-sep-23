# Ad Hoc Queries with the metadata database
- Refer:
  - docker-compose-LocalExecutor.yml
  - Dockerfile
    - Based on Python 3.7
    - ARG
    - Env Variables
    - Expose

  - entrypoint.sh
    - export
    - Refer - AIRFLOW__CORE__SQL_ALCHEMY_CONN
    - Refer - AIRFLOW__CELERY__RESULT_BACKEND
  - airflow.cfg
    - sql_alchemy_conn
      - Will be overwritten by AIRFLOW__CORE__SQL_ALCHEMY_CONN as specified in the env variable in entrypoint.sh
  - Run
  ```
  ls
  docker-compose -f docker-compose-LocalExecutor.yml up -d
  docker ps  
  ```
  - Open Airflow UI
  - Create connection - Admin\Connections
    - Conn Id: postgress_1
    - Conn Type: Postgress
    - Host: postgress
    - Schema: airflow
    - Login: airflow
    - Password: airflow
    - Port: 5432
  - Turn on parallel_dag
  - Click on Data Profiling\Add Hoc Query
  - Select the connection we created
  - Run below queries one by one:
    - List the Airflow tables in PostgreSQL
    ```
    SELECT * FROM
    pg_catalog.pg_tables
    WHERE
    schemaname != 'pg_catalog'
    AND schemaname != 'information_schema'
    AND tableowner = 'airflow';
    ```
    - List the task instances
    ```
    SELECT * FROM task_instance;
    ```
    - List the dag runs
    ```
    SELECT * FROM dag_run;
    ```
    - Get total completed task count
    ```
    SELECT COUNT(1) FROM task_instance
    WHERE state IS NOT NULL
    AND state NOT IN ('scheduled', 'queued');
    ```
    - Get tasks started per minute for the past week
    ```
    SELECT date_trunc('minute', start_date) AS d, count(1)
    FROM task_instance
    GROUP BY d
    ORDER BY 1 DESC
    LIMIT 24*7;
    ```

    - Get tasks finished per minute for the past week
    ```
    SELECT date_trunc('minute', end_date) AS d, count(1)
    FROM task_instance
    WHERE state IN ('skipped', 'success', 'failed')
    AND end_date IS NOT NULL
    GROUP BY d
    ORDER BY 1 DESC
    LIMIT 24*7;
    ```

- Now as we see that anyone having access to Airflow UI can access our data. Its not a very secure thing. We can turn this feature off
- Modify airflow.cfg - secure_mode = True
- Restart
```
docker-compose -f docker-compose-LocalExecutor.yml down
docker-compose -f docker-compose-LocalExecutor.yml up -d
```
- Now Data Profiling\Add Hoc Query is not available
