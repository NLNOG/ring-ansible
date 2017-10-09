#!/usr/bin/env bash

/usr/sbin/birdc show route primary all | egrep "unreachable|as_path" | paste - - | sed 's/{.*//' | awk '{ print $1 " " $NF }' | grep -v "^0\.0\.0\.0/0 " | sort -n -k 2 > /usr/share/nginx/www/table-v4.txt.tmp
/usr/sbin/birdc6 show route primary all | egrep "unreachable|as_path" | paste - - | sed 's/{.*//' | awk '{ print $1 " " $NF }' | grep -v "^::/0 " | sort -n -k 2 > /usr/share/nginx/www/table-v6.txt.tmp

mv /usr/share/nginx/www/table-v4.txt.tmp /usr/share/nginx/www/table-v4.txt
mv /usr/share/nginx/www/table-v6.txt.tmp /usr/share/nginx/www/table-v6.txt
cat /usr/share/nginx/www/table-v4.txt /usr/share/nginx/www/table-v6.txt > /usr/share/nginx/www/table.txt.tmp
mv /usr/share/nginx/www/table.txt.tmp /usr/share/nginx/www/table.txt
