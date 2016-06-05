#!/bin/bash
# script to compile a big and small font version  -jbsilva

source params_thesis.bash

sed -i 's/12pt/11pt/g' $thesis_prefix.tex   
./compileLatex.sh $thesis_prefix
mv $thesis_prefix.pdf ${thesis_prefix}_sm.pdf

sed -i 's/11pt/12pt/g' $thesis_prefix.tex  
./compileLatex.sh $thesis_prefix

./packageForPush.sh
