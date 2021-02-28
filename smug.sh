#!/bin/bash 

mkdir -p ./smug

function smugg(){
	filename=$(echo $1 |sha256sum |awk '{print $1}')
	echo "$1  $filename" >> ./smug/index.txt
	python3 ~/tools/smuggler/smuggler.py -u $1  -q  -x  -l ./smug/$filename 
	
}

export -f smugg 
cat $1 |xargs -n 1 -P 100  -I {} bash -c 'smugg "$@"' _ {}
