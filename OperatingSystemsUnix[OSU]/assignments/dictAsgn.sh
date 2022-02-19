#!/bin/bash
choice="Select an option: "
select i in "Words with a length like 'n'" "Words ending with a letter like 'q'" "Words starting with a letter like 'p'" "Words starting with a substring like 'par'" "Words ending with a substring like 'lps'" "exit"
do
case $REPLY in
1) read -p "Length: " length
   grep -E "^.{$length}$" /usr/share/dict/american-english;;
2) read -p "Ending Letter: " letter
   grep -o "\w\+$letter" /usr/share/dict/american-english;;
3) read -p "Starting Letter: " letter
   grep -o -E "^$letter.*" /usr/share/dict/american-english;;
4) read -p "Starting Substring: " subs
   grep -o -E "^$subs.*" /usr/share/dict/american-english;;
5) read -p "Ending Substring: " ends
   grep -o -E "^.*$ends" /usr/share/dict/american-english;;
6) exit;;
*) echo WRONG CHOICE;;
esac
break
done

