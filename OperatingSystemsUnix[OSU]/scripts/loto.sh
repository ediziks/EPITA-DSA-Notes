echo Please choose your game
echo "1) Loto"
echo "2) Euromillion"
read -p "Please enter your choice: " choice

case $choice in
1)
shuf -n 5 -i 1-49 | tr -s '\n' ' '
echo -n "your luck number is:" 
shuf -n 1 -i 1-10
;;
2)
shuf -n 5 -i 1-50
echo -n "your stars: "
shuf -n 2 -i 1-12
;;
*) echo you are from another planete, go play far away
;;
esac
