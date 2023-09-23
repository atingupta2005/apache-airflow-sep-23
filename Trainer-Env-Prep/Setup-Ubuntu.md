# Trainer Tasks
## Setup multiple users in Ubuntu
- For each participant, we need to setup login accounts
```
sudo groupadd docker


for ((i=1;i<=9;i++)); do
	export username="u0$i"
	sudo useradd -g docker -m -p "p" $username;sudo usermod -aG sudo $username;echo $username:p | sudo /usr/sbin/chpasswd;sudo chown -R  $username:root /home/$username
done


for ((i=10;i<=50;i++)); do
	export username="u$i"
	sudo useradd -g docker -m -p "p" $username;sudo usermod -aG sudo $username;echo $username:p | sudo /usr/sbin/chpasswd;sudo chown -R  $username:root /home/$username
done
```

## Install docker
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
sudo usermod -aG sudo $USER
sudo apt -y install docker-compose
```
