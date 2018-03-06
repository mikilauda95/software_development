#! /bin/sh

egrep '<div class="num-votes"|<div class="command">'|awk -F "[><]" '{print }'|egrep -v '^$'| sed -r 's/<div class="command">|<div class="num-votes" id="num-votes-[0-9]*[0-9]">//' | sed -r 's-</div>--' | sed 's/^[ \t]*//' | awk 'BEGIN{RS=""; FS="\n"} {for(i=1;i<=NF/2;++i) {if(($(2*i)+0)>=5){print $(2*i-1)}}}' 

#egrep '<div class="num-votes"|<div class="command">'|awk -F "[><]" '{print }'|egrep -v '^$'| sed -r 's/<div class="command">|<div class="num-votes" id="num-votes-[0-9]*[0-9]">//' | sed -r 's-</div>--' | sed 's/^[ \t]*//' | awk 'BEGIN{RS=""; FS="\n"} {for(i=1;i<=NF;i++) print $i}' 

#| awk 'BEGIN{FS="\n";RS=""}' '{for(i=1;i<=NF;i++) print $i}' 
# | sort |uniq -c| sort -nr|sed -r 's/^[ \t]*//'
#if(($(i+1)+0)>=5){print $i}}
#{for(i=1;i<=NF/2;i++){print $(2*i-1) $(2i)}
#| egrep -B1 '^[5-9]|[1-9]*[1-9][0-9]$'|egrep -v '^--$'|egrep -v '^[0-9]+$'
