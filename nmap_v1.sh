#!/bin/bash

##### WORK IN PROGRESS - Just trying to learn bash scripting #####

nmap $1 > nmap_output.txt
echo $1

port_no="$(grep vnc nmap_output.txt | awk '{print $1}')"
echo $port_no

just_port="$(sed -i 's/\/tcp/,/g' $port_no)"
echo $just_port

# VAR="$(grep word /path/to/file)"
# grep ^hello file | awk '{print $2}'
# first="I love Suzy and Mary"
# second="Sara"
# first=${first/Suzy/$second}
# sed -i 's/old-text/new-text/g' input.txt

echo "Script Finished"