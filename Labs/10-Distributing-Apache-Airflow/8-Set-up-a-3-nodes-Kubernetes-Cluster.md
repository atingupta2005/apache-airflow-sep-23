# Set up a 3 nodes Kubernetes Cluster
- Install Virtual Box
- Install Vagrant
- Refer Vagrantfile
- Install K8S cluster and connect to master
```
cd vagrant-files
vagrant plugin install vagrant-vbguest vagrant-scp
ls
vagrant up
vagrant status
vagrant ssh master
```

- Run commands on master
```
kubectl get pods
kubectl get nodes
```
- Troubleshooting
```
vagrant reload worker-1
vagrant reload worker-2
vagrant reload master
```

## Install Rancher
- Rancher is for deploying and managing K8S
- It makes simple what you will take a lot of time to set up with the Kubernetes command line interface by providing a nice user interface
- Setup Rancher
```
docker run -d --restart=unless-stopped -p 80:80 -p 443:443 --name rancher rancher/rancher:v2.3.2
docker ps
```

- Open Web Browser - localhost and open rancher dashboard
- Click Add Cluster
- Import existing cluster
- Cluster Name: airflow
- Click Create
- Import cluster into rancher
- Copy the last command and run on terminal of master
- Open browser and click Done
- Wait for few minutes
- Now it's active
- Browse through the UI
