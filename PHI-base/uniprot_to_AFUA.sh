#!/bin/bash
#1 is a file that contains all uniq uniprot ids
#2 is the conversion file that was originally made in excel
while read LINE; do
    AFUA=$(grep -w "$LINE" $2 | cut -f7,7)
    echo $LINE $AFUA
done < $1
