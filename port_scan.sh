#!/bin/bash

#nmap -p 80,81,300,443,591,593,832,981,1010,1311,1099,2082,2095,2096,2480,3000,3128,3333,4243,4567,4711,4712,4993,5000,5104,5108,5280,5281,5800,6543,7000,7396,7474,8000,8001,8008,8014,8042,8069,8080,8081,8083,8088,8090,8091,8118,8123,8172,8222,8243,8280,8281,8333,8337,8443,8500,8834,8880,8888,8983,9000,9043,9060,9080,9090,9091,9200,9443,9800,9981,10000,11371,12443,16080,18091,18092,20720,55672 $1

$host=$1

cat  $1 | xargs	dig {} +short |grep -Po "([0-9]{2,3})(\\.[0-9]{1,3}){3}" >> ips


masscan -p0-79,81-442,444-65535 -iL ips --rate=10000 -oB temp


masscan --readscan temp |awk '{print $NF":"$1}' |cut -d / -f 1 open_port 