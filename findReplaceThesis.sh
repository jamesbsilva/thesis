#!/bin/bash
# script to change word across all thesis  -jbsilva
sed -i "s/$1/$2/g" chapter0.tex
sed -i "s/$1/$2/g" chapter1.tex
sed -i "s/$1/$2/g" chapter2.tex
sed -i "s/$1/$2/g" chapter3.tex
sed -i "s/$1/$2/g" chapter4.tex
sed -i "s/$1/$2/g" chapter5.tex
sed -i "s/$1/$2/g" chapter6.tex
sed -i "s/$1/$2/g" chapter7.tex
sed -i "s/$1/$2/g" chapter8.tex
sed -i "s/$1/$2/g" chapter9.tex
sed -i "s/$1/$2/g" chapterZ.tex



