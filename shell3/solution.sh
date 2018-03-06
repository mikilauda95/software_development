#! /bin/sh

find_dir(){
  find $1 -maxdepth 1 -type d| egrep -v '^'"$1"'$'
}
find_recents(){
  dirname $(find $1 -atime -30 -type f) 
}
find_not_recents(){
  find $1 -atime +30 -type f
}

#for debugging_purpose
get_files(){
  dirname $(find_not_recents .) > ../not_recents | sed -r 's-^.[/]?--'
  dirname $(find_recents .) > ../recents | sed -r 's-^.[/]?--'| awk 'BEGIN{OFS="/";FS="/"}{for(i=1;i<=NF;i++){for(j=1;j<=i;j++)print $i;}print '\n'}'

}

#in recents scompatta le directory in subdirectories
#in not recents prendi la directory padre
#fai l'operazione directories in not recents ma non in recent

#awk 'BEGIN{OFS="/";FS="/"}{for(i=1;i<=NF;i++){for(j=1;j<=i;j++)print $i;}print '\n'}'



#dirname $(find_recents .) | sed -r 's-^.[/]?--'| awk 'BEGIN{OFS="/";FS="/"}{for(i=1;i<=NF;i++){for(j=1;j<=i;j++) {print $j;} print '\n'}}'

save_space(){
  find_recents $1> /dev/null
  if [ $? -eq 0 ] 
    then #if find_recents fails ? is 1; it could fail if there are no dir or if it can be compressed
      a=$(find_dir $1)
      for i in $a
      do
        save_space $i
      done
    else 
      tar -zcvf $1.tgz $1
      rm -r $1
    fi
}

#execute it
save_space .

#save_space pwd

#save_space(){
  #echo $1
  #find_recents $1 >/dev/null
  #if [ $? -eq 0 ] 
    #then #if find_recents fails ? is 1; it could fail if there are no dir or if it can be compressed
    #save_space $(find_dir $1) >/dev/null
  #else 
    #echo $pwd
  #fi
#}
