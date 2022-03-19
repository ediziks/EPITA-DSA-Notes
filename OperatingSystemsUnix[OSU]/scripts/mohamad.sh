for i in $(ls)
do

nm=$(echo $i | tr A-Z a-z)
mv -v $i $nm
done 
