# Set up a custom XCom backend

## Set up your object storage account
- Log into your Google Cloud account and create a new project called custom-xcom-backend-airflow.
- Create a new bucket called gcs-xcom-backend-airflow.
- Create a custom IAM role called AirflowXComBackendGCS for Airflow to access your bucket. Assign 6 permissions:
  - storage.buckets.list
  - storage.objects.create
  - storage.objects.delete
  - storage.objects.get
  - storage.objects.list
  - storage.objects.update

- Create a new service account called airflow-xcom and grant it access to your project by granting it the AirflowXComBackendGCS role.

## Create a connection
- To give Airflow access to your GCS bucket you need to define an Airflow connection.

- In the Airflow UI go to Admin -> Connections and create a new a connection (+) with the Connection Type Google Cloud. Provide the name of your connection (gcs_xcom_backend_conn)
- Open the JSON file with the credentials you downloaded in previous step and copy paste it in full into the field Keyfile JSON.

## Define a custom XCom class
- Refer - xcom_backend_pandas.py

- Put xcom_backend_pandas.py into the $AIRFLOW_HOME/plugins directory

- Add the following line to set your XCom backend to the custom class:

## Create a custom serialization method to handle Pandas dataframes
[core]
xcom_backend=xcom_backend_pandas.CustomXComBackendPandas

## Run a DAG passing Pandas dataframes via XCom
- Refer: fetch_pokemon_data_dag.py

