#! /bin/sh

egrep '^<div class="comment">'|awk -F "[><]" '{print $5}' | sort |uniq -c| sort -nr|sed -r 's/^[ \t]*//'
