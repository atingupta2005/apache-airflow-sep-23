# Configure CLI

## Login to GCP
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


### Connect CLI to Composer CLI
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
