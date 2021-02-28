#!/bin/bash 

touch nuclei_result 

tele nuclei_result &

cat $1 |xargs - 1 -P 20 bash -c " nuclei  -t ~/ncl/costum_tmp/$2  -target {} -timeout 10  -retries 2 |tee -a nuclei_result "
