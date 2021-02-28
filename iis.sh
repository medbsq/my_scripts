#!/bin/bash 

mkdir -p iis
for i in $(cat $1);do
	file="$(echo $i |cut -d "/" -f 3)"
#	java -jar ~/IIS-ShortName-Scanner/iis_shortname_scanner.jar 2 20 "$i" |tee -a iis/$file
	echo $file
done


