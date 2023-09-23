## Login to GCP
- 

## Create Composer resource
- 

## Setup DAG Folder of GCP Composer

### Install gcloud sdk (One time)
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

## Install gcsfuse to mount DAG Folder
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


### Connect CLI to Composer CLI
```
sudo apt-get install kubectl -y
```

```
sudo apt-get install google-cloud-sdk-gke-gcloud-auth-plugin
```


