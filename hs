#!/bin/bash


function send(){
        host="$(echo $1 |sha256sum |awk '{print $1}').$2"
        echo "$1   $host"  >> hash
        echo $1 |httpx -H "Host: $host" 
}

for i in $(cat $1);do 
        send $i $2
done

