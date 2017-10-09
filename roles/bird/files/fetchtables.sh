#!/usr/bin/env bash

/usr/sbin/birdc show route primary all | egrep "unreachable|as_path" | paste - - | sed 's/{.*//' | awk '{ print $1 " " $NF }' | grep -v "^0\.0\.0\.0/0 " | sort -n -k 2 > /var/www/html/table-v4.txt.tmp
/usr/sbin/birdc6 show route primary all | egrep "unreachable|as_path" | paste - - | sed 's/{.*//' | awk '{ print $1 " " $NF }' | grep -v "^::/0 " | sort -n -k 2 > /var/www/html/table-v6.txt.tmp

mv /var/www/html/table-v4.txt.tmp /var/www/html/table-v4.txt
mv /var/www/html/table-v6.txt.tmp /var/www/html/table-v6.txt
cat /var/www/html/table-v4.txt /var/www/html/table-v6.txt > /usr/share/nginx/www/table.txt.tmp
mv /var/www/html/table.txt.tmp /var/www/html/table.txt
