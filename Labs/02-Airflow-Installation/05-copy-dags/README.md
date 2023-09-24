cd ~
git clone https://github.com/atingupta2005/apache-airflow-sep-23
#git stash
cd ~/apache-airflow-sep-23/Labs/Airflow-Dags-Hands-on
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

 replacec="dag_id="
 replacewithc="tags=['$USER', '$FILEPATH', '$FILENAME'], dag_id="
 sed -i "s/$replacec/$replacewithc/g" $FILEPATH/$new_file_name
done

ls 1
cat 1/atingupta2005-1-00_umbrella.py

rm -rf ~/mnt/composer/dags/$USER
mkdir ~/mnt/composer/dags/$USER
cd ~/apache-airflow-sep-23/Labs/Airflow-Dags-Hands-on
cp -r . ~/mnt/composer/dags/$USER
ls ~/mnt/composer/dags

rm -rf /airflow/dags/$USER
mkdir /airflow/dags/$USER
cd ~/apache-airflow-sep-23/Labs/Airflow-Dags-Hands-on
cp -r . /airflow/dags/$USER
ls /airflow/dags/$USER