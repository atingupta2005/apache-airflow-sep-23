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
