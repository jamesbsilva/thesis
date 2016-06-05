#!/bin/bash
# script to find used files for cleaning  -jbsilva

dir_to_search=$1
filetype_to_search=$2

arr=$(find ./$dir_to_search/ -iname "*.$filetype_to_search")
for file in $arr; do
	filename="${file##*/}"
	clean_file=$(echo "$filename" | sed "s/$filetype_to_search//g")
	search_res=$(grep -i "$clean_file" ./*.tex)
	if [ "${#search_res}" -gt 0 ] 
	then 	
		echo "File Found: $filename"	
	else
		rm $file
	fi
done
