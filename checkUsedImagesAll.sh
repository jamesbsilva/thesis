#!/bin/bash
# script to find used files for cleaning  -jbsilva

./checkUsedImages.sh Figures pdf
./checkUsedImages.sh Figures png
./checkUsedImages.sh Figures jpg
./checkUsedImages.sh Figures jpeg

./checkUsedImages.sh Images pdf
./checkUsedImages.sh Images png
./checkUsedImages.sh Images jpg
./checkUsedImages.sh Images jpeg

