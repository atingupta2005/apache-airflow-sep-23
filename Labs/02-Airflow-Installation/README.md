# Airflow Installation
- Using Production Docker Images
- Using Official Airflow Helm Chart
- Using GCP Managed Airflow Services
- Using 3rd-party images, charts, deployments

## Using Managed Airflow Services
- When you prefer to have someone else manage Airflow installation for you, there are Managed Airflow Services that you can use.
- Airflow Community does not provide any specific documentation for managed services. Please refer to the documentation of the Managed Services for details.

## Setup DAG Folder
### Install gcloud sdk
```
sudo apt-get update
```

```
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
```

```
sudo apt-get install apt-transport-https ca-certificates gnupg
```

```
sudo apt-get install curl
```

```
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
```

```
sudo apt-get update && sudo apt-get install google-cloud-sdk
```

```
gsutil version -l
```

```
gcloud auth login --no-launch-browser
```

```
gcloud config set project learned-pottery-399802
```

## Mount DAG Folder
```
export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s` 
```

```
echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list
```

```
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
```

```
sudo apt-get update
```

```
sudo apt-get install gcsfuse
```

```
mkdir -p ~/mnt/composer
```

```
ls -al ~/mnt/composer
```

```
gcloud auth application-default login --no-launch-browser
```

```
gcsfuse asia-east2-composer-1-f50dc24e-bucket "~/mnt/composer"
```

```
ls ~/mnt/composer
```

```
cd ~/mnt/composer
```

```
tree .
```


### Connect CLI to Composer CLI
```
sudo apt-get install kubectl -y
```

```
sudo apt-get install google-cloud-sdk-gke-gcloud-auth-plugin
```

```
cat ~/.bashrc
```

```
echo "export USE_GKE_GCLOUD_AUTH_PLUGIN=True" >> ~/.bashrc
echo 'alias GCPCMPSR="gcloud composer environments run composer-1 --location asia-east2"' >> ~/.bashrc
```

```
cat ~/.bashrc
```

```
source ~/.bashrc
```

```
GCPCMPSR dags list -- --output=json
```