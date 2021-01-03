#!/bin/sh

total=0
echo -e "Hour\tNumber of points"
for hour in $(seq -f "%02g" 0 23)
do
    
    number=$(cat "$1" | grep ",$hour:" | wc -l)
    echo -e "$hour\t$number"
    total=$((total+number))
done
echo -e "\nTotal:\t$total"
