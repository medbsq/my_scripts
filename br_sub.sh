#!/bin/bash 
for asset in $(cat $1 );do
	cat $1 |xargs -n 1 -P 100 -I {} bash -c 'echo "{}.$1" |tee -a prob_dom.txt'
done 
