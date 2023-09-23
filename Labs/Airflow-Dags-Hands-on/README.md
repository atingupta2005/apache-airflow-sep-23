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
for FULLFILEPATH in */*; do 
 replace="/"
 replacewith="-"
 #echo $FULLFILEPATH
 FILENAME=$(echo $FULLFILEPATH | cut -d'/' -f2)
 FILEPATH=$(echo $FULLFILEPATH | cut -d'/' -f1)
 new_file_name="$USER-$FILEPATH-${FILENAME/$replace/$replacewith}";

 replacec=$(echo $FILENAME | awk '{ print substr( $0, 1, length($0)-3 ) }')
 replacewithc=$(echo $new_file_name | awk '{ print substr( $0, 1, length($0)-3 ) }')
 
 mv $FULLFILEPATH $FILEPATH/$new_file_name
 sed -i "s/$replacec/$replacewithc/g" $FILEPATH/$new_file_name
done
```


```
mkdir -p ~/mnt/composer/dags/$USER
```


```
cp -r . ~/mnt/composer/dags/$USER
```

```
rm -rf ~/mnt/composer/$USER
```

```
ls ~/mnt/composer/dags
```
