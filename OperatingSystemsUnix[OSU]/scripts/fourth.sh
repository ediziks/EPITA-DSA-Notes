echo -n "Please provide your luck number: "
read lnb

if [ $lnb -eq 7 ]
then
	echo True: you are lucky
elif [ $lnb -lt 7 ]
then
	echo must be greater
echo try again
else
echo you are not lucky
echo yet another commad
fi
