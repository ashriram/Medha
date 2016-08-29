#!/bin/sh
echo '---------------------------------------------'
echo 'Now downloading all videos from videoList.txt'
echo '---------------------------------------------'

counter=0;
while read p;
  counter=$((counter+1))
 # echo $counter	
  do   ./test.rb "$p" ;
  done < Names.txt
echo "total".$counter