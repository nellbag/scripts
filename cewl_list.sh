#!/bin/bash


if [[ $# -eq 0 ]] ; then
    echo "Incorrect syntax! Please provide an input list and a spider depth (min 1):"
    echo "e.g. ./cewl_list.sh ./websites.txt 2 "
    exit 0
fi

echo "Starting..."
touch temp_cewl.txt

while IFS="" read -r p || [ -n "$p" ]
do
    echo "Crawling website: $p"
    cewl $p -d $2 --with-numbers >> temp_cewl.txt
    count=$(wc -w temp_cewl.txt | awk 'NR==1{print $1}')
    echo "Total: $count words"
done < $1

sort temp_cewl.txt | uniq -u > output.txt
count=$(wc -w output.txt | awk 'NR==1{print $1}')
rm temp_cewl.txt

echo "$count unique words found." 
echo "See output.txt for results."
