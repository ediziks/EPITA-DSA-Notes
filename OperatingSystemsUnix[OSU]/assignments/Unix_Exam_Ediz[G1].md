# Unix Exam - [G1]

### Exercise 1

1.1) What is the difference between Unix and Linux?

Linux stands for the kernel of the operating system (GNU/Linux), it refers to the family of obtained distributions. And, Unix refers to the original operating system, to family of derived operating systems.

Indeed, Linux is open source, and in Unix, the source code is proprietary.

1.2) What is MINIX? Who is the author?

MINIX is developed in 1987 by Andrew Stuart Tanenbaum as a teaching tool. It is mainly a text-oriented operating system with a kernel less than 6000 lines of code.

1.3) Author of Linux? Relationship between linux and minix?

Linus Torvalds is the author of Linux. MINIX was used to build Linux. Torvalds and Tanenbaum were student and teacher of each other, they had disagreed on Torvalds’ decision to design Linux as monolithic kernel, rather than a micro-kernel, which MINIX was.

1.2*) Command to display the version of your Linux kernel? 

- how to know if kernel is stable or not?

$ uname -r  *→  is the command to display the version of Linux kernel*

Linux versions including LTS (Long Term Support) in their version names refers to the stable branches, and the ones without LTS are unstable (normal) releases that do not get updates after a while.

*: Likely a typo in Exercises

1.3*) command to change the directory to /etc

- which files are in /etc

$ cd /etc *→ changes directory to /etc path*

There are configuration files related to OS under /etc, such as user credentials.

1.5) ls -ltr

To list the contents of the current directory in the long listing format (`l`), sorted by modification time (`t`) in reverse order (`r`) of all files and directories.

1.6) cp -r /home/osman/EPITA /home/backup

Both commands are to copy the directory in the first argument to the second one, recursively. There are no any differences between (`-r`), (`-R`), and `--recursive`)

1.7) cat -n /etc/group

`cat` shows what a file includes in it. `cat -n` is shows together with the line numbers.

1.8) chmod ugo+rw file.txt / chmod 666 file.txt

Both commands do add the read and write permissions user, group and others but executable function. So, there is no any significant difference between those commands. Both changes `rwxrwxrwx` to `rw-rw-rw-`

1.9) ls -a / ls -A

`ls -a` → meaning `--all`, does not ignore entries starting with .

`ls -A` → meaning `--almost-all`, does not list implied . and ..

1.10) mkdir -p dir1/subdir1/small
Creates the small directory in the given path. `-p` option helps to create parents directories if they do not exist

1.11) `date +%s`
Shows the second of the date/time that computer already set on

1.12)
13- `ln -v file.txt hshortcut`
14- `ln -s file.txt ssorthcut`

1.13) `wc -lwc file.txt`
`-l`: prints the count of lines that are there in the file.txt
`-w`: prints the number of words that are there in the file.txt
`-c`: prints the number of bytes present in the file.txt

1.14) Display only the before last line from a given file "file.txt"
`tail -n 2 file.txt | head -n 1`

1.15) chmod ugo+rw file.txt / chmod 620 file.txt
`chmod ugo+rw file.txt` gives read and write permissions to user, group of users and others, and changes permission from `-rwxr--r--` to `-rwxrw-rw-`

`chmod 620 file.txt` users receive read and write permissions, group of users receive write permissions and others will have permissions as earlier. Changes permission from `-rwxr--r--` to `-rwxrw-r--`

1.16)

```bash
for i in 1 2 3 4 5 .. N
do
  cmd1
  cmd2
  cmdN
done
```

```bash
while [ condition ]
do
  cmd1
  cmd2
  cmdN
done
```

```bash
select i in <list>
do
  [commands]
done
```

```bash
until [ condition ]
do
 [ commands ]
done
```

```bash
func1 {
  [ commands ]
}

func2 {
  func1
}
```

1.17)
`read -s var` → Will not display on the screen and is stored in var

`read -n 8 var` → The user input will restricted with a specific threshold of 8 characters and prompt will automatically vanish after 8 characters
`read -t 2 var` → The user input will be restricted for 2 for a timeperiod of seconds and will vanish after 2 seconds
`read -p "Could you please enter the value of the variable :" var` → Prompts a message to the screen which is stored in var

1.18) Difference between `;`, `||`, `&&` 

`ls -l ; mkdir directory; cd directory; touch f{1..9}` → Commands will be executed one by one
`ls -l` → Displays the files in current directory
`mkdir directory` → Creates a directory named directory
`cd directory` → changes the directory to directory

`touch f{1..9}` → Creates files named f1 to f9

`ls -l file.txt || echo the file does not exist` →"echo the file does not exist " will execute if there is no file.txt, file.txt will be listed if there is file in current directory if there is no file, then the command 2 will get executed	
`ls -l file.txt && echo the file exist`
"echo the file exist" will execute if "ls -l file.txt" has executed successfully.
the file exist is displayed on output if the file.txt exists in current directory

### Exercise 2

1

```bash
jenny
$person
jenny
```

2

```bash
Looping ... number 1
Looping ... number 2
Looping ... number 3
Looping ... number 4
Looping ... number 5
```

3

```bash
1 ... 2
2 ... 4
3 ... 6
4 ... 1
5 ... 3
6 ... 5
7 ... 7
DONE!
```

4

```bash
34
FREDO.tar.gz
FREDO.tar.gz
fredo.tar.gz

fred
/home/jean/fredy/Siso/fred7.tar.gz
/home/jean/jeany/Siso/jean7.tar.gz
/home//fredy/Siso/fred7.tar.gz
/home//y/Siso/7.tar.gz
tar.gz
fred7.tar.gz
/home/fred/fredy/Siso

FREDO.tar.gz
FREDO.TAR.GZ
fREDO.tar.gz
fredo.tar.gz

/home/fred/fredy/Siso/fred7.tar.gz
/HOME/FRED/FREDY/sISO/FRED7.TAR.GZ
Ahmed
Ahmed Alexandre Alice Bob Charlie
5
Ahmed[1]
Alice
5
0 1 2 3 100
exa
```

5

```bash
the result of 4, 8 and 21 is 11
the average of 4 and 14 is 9
the average of nothing is 0
```

6

```bash
The res1 of 1 is 1
The res2 of 1 is 1
The res1 of 2 is 4
The res2 of 2 is 8
The res1 of 3 is 9
The res2 of 3 is 27
The res1 of 4 is 16
The res2 of 4 is 64
The res1 of 5 is 25
The res2 of 5 is 125
```

7

Explanation: There are 2 possible scenarios for the output for this script. 

1st case: *if we do not have any .doc file in the current directory;*

→ `mv: cannot stat '*.doc': No such file or directory`

2nd case: *if we do have a .doc file within the directory*

→ “*No output”*

### Exercise 3

3.1

```bash
#!/bin/bash
game="Select your game: "
select i in "Loto" "Euro Million" "exit"
do
case $REPLY in
1) ( echo Numbers:; shuf -i 1-49 -n5; echo Lucky:; shuf -i 1-10 -n1 ) | xargs -n8;;
2) ( echo Numbers:; shuf -i 1-50 -n5; echo stars:; shuf -i 1-12 -n2 ) | xargs -n9;;
3) exit;;
*) echo wrong choice;;
esac
done
```

3.2

```bash
#!/bin/bash
if ! [[ -e $@ ]]
then
  echo Verification des arguments reussie
else
  echo Aucun argument fourni
fi
dt=$(date '+%d_%m_%Y_%H_%M_%S');
red="\033[0;31m"
nc="\033[0m"
echo "Ce script a pour objectif de realiser une sauvegarde :"
select i in "Avec une extension tar.gz" "Avec une extension tar.bz2" "Avec une extension tar.xz"
do
  case $REPLY in
    1) tar -czvf backup$dt.tar.gz $(echo $@); echo -e "Fichiers/Dossiers compresses dans ${red}backup${dt}.tar.gz${nc}";;
    2) tar -cjvf backup$dt.tar.bz2 $(echo $@); echo -e "Fichiers/Dossiers compresses dans ${red}backup${dt}.tar.bz2${nc}";;
    3) tar -cJvf backup$dt.tar.xz $(echo $@); echo -e "Fichiers/Dossiers compresses dans ${red}backup${dt}.tar.xz${nc}";;
    *) echo "Mauvais choix!"
  esac
exit
done

### ~ Usage ~ ###
# $ ./script.sh ./anyAmountOfFolders ./anyAmountOfFile
```

3.3

```bash
#!/bin/bash
rm marks.txt
touch marks.txt
nmark=1
regint='^[0-9]+$'
echo 'Enter a "mark" or press "q" to indicate the end of the entry: '
while read -r -p "Mark $nmark: "
do
if [[ $REPLY =~ $regint ]]
  then
    let nmark+=1
fi
case $REPLY in
  q) awk '{ if ($1~/^[0-9]+$/) n++ } END { if (n>0) print "a) Number of marks: " n }' marks.txt;
     awk '{ if ($1<1) { } else if ($1~/^[0-9]+$/) { sum+=$1; n++ }} END { if (n!=0) print "b) Avg: " sum/n }' marks.txt;
     awk 'BEGIN { a=0 } { if ($1>0+a) a=$1; n++ } END { if (n>0) print "c) Max: "  a }' marks.txt;
     awk 'BEGIN { a=1000 } { if ($1<0+a && $1~/^[0-9]+$/) a=$1; n++ } END { if (n>0) print "d) Min: "  a }' marks.txt;
     awk 'BEGIN { low=0 } { if ($1<1) { } else if ($1<10) { low++; n++ }} END { if (n>0) print "e) # of Marks Below 10: "  low }' marks.txt;
     break;;
  ''|*[0-9]*) echo $REPLY >> marks.txt;;
  *) echo only marks or q;;
esac
done
```

3.4

```bash
#!/bin/bash
[ $# -ne 3 ] && echo number of argument must be 3 && exit 2
case $2 in
+) echo $(($1 + $3))
;;
-) echo $(($1 - $3))
;;
x) echo $(($1 * $3))
;;
/) echo $(echo "scale=2; $1 / $3" | bc -l )
;;
pow) echo $(($1 ** $3))
;;
mod) echo $(($1 % $3))
;;
esac

### ~ Usage ~ ###
# $ ./script.sh 4 pow 2
```

3.5

```bash
#!/bin/bash
[ $# -ne 1 ] && echo number of argument must be 1 && read -r -p "Enter a number to be factorialized: " num
if [ $# -eq 1 ]
  then
  num=$1
fi

result=1

while [ $num -gt 1 ]
do
  result=$(( result * num))
  num=$((num - 1))
done

echo $result
```

3.6

```bash
#!/bin/bash
echo "Value + Enter to sort the array, press q to end: "

while read line
do
  if [ "$line" = "q" ]
    then
      break
  else
    arr=("${arr[@]}" $line)
  fi
done

arr=($(echo ${arr[@]} | tr " " "\n" | sort -n))
echo "Sorted array =" ${arr[@]}
```

3.7

```bash
#!/bin/bash
wc -m $1 | awk '{print $1}'
```

3.8

```bash
#!/bin/bash
echo "obase=2;$1" | bc
echo "obase=8;$1" | bc
echo "obase=16;$1" | bc
```

3.9

```bash
#!/bin/bash
count=0
spec="#!/bin/bash"
for file in ./*;
do
  if [[ -f $file ]] && [[ "$(head -n 1 $file)" == "$spec" ]]
  then
    let count+=1
    echo "${count}) ${file}"
  fi
done
```

3.10

```bash
#!/bin/bash
cmd=$(grep -iwF $1 /usr/share/dict/french)
if [ $? != 0 ]
then
  echo No match
else
  echo "Exists @" $cmd
fi
```

3.11

```bash
#!/bin/bash
format=$(date -d "$2/$1/1 + 1 month - 1 day" "+%Y %b - %d days")
echo "$format"

### ~ Usage ~ ###
# $ ./script.sh 2 2024
# 2024 Feb - 29 days
```

3.12

```bash
#!/bin/bash
for i in ./*
do
  if [ -f $i ]
  then
    for y in ./*
    do
      if [ -f $y ] && [ $i != $y ]
      then
        diff $i $y >/dev/null
        if [ `echo $?` -eq 0 ]
        then
          echo $i and $y have the Same content
          echo So $y is deleting now...
          rm $y
        else
          echo $i and $y are Different
        fi
      fi
    done
  fi
done
```

3.13

```bash
#!/bin/bash
find . -name "*" -type 'f' -size +100M -delete
```

3.14

```bash
#!/bin/bash
echo "$1" | awk '{ print toupper($0) }'
```

### Exercise 4

`5` → number of characters in the first element of the array

`4` → length of the array

`5` → length of the first (0th place) element of array

`6` → length of the second (1st place) element of array

`4` → length of the third (2nd place) element of array

`6` → length of the fourth (3rd place) element of array

`orange` → fourth (3rd place) element of array

`pear orange` → elements in range of 2nd to 3rd

4.2

`fruits=("aa" "${fruits[@]}")`

4.3

`fruits+=(gg)`

4.4

`fruits=( "${fruits[@]:0:3}" "dd" "${fruits[@]:3}" )`

### Exercise 5

1

`cat /etc/squid/squid.conf | grep -E '^.{3}$'`

2

`cat /etc/squid/squid.conf | grep -E '^.{3,}$'`

3

`cat /etc/squid/squid.conf | grep -E '^.{0,3}$'`

4

`cat /etc/squid/squid.conf | grep -cE '^.{0}$'`

5

`cat regtest | grep -E '^[^A-G]'`

6

`grep -E '^[^ #]' /etc/squid/squid.conf > tmp && sudo mv tmp /etc/squid/squid.conf`

7

```bash
sed '1,25s/squid/squid3/g' /etc/squid/squid.conf # > tmp && sudo mv tmp /etc/squid/squid.conf

# commented bit of code or `sed -i` can be used to change the file permanently
# can also be used for the answers below here if needed
```

8

`sed 's/squid/squid3/g' /etc/squid/squid.conf`

9

`sed '/ACL/Id' /etc/squid/squid.conf`

10

`sed '1,9!d' /etc/squid/squid.conf`

11

`sed '/src/d' /etc/squid/squid.conf`

12

`sed 's/#.*$//;/^$/d' /etc/squid/squid.conf`

### Exercise 6

```bash
#!/bin/bash
red="\033[0;31m"
nc="\033[0m"
echo -e "${red}Name   Avg  Min Max${nc}"
awk -F ";" '{ min=$4; max=$4; for(i=4;i<=NF;i++) if ($i>max) { max=$i } else if ($i<min) { min=$i } print $1, ($4+$5+$6+$7+$8+$9)/6, min, max }' marks.csv
```