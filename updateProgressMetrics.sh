#!/bin/bash
# script to find calculate metrics such as pagecount  -jbsilva

source params_thesis.bash

pgsIn="$(pdfinfo $thesis_prefix.pdf | grep ^Pages:)"
wrdsInH="$(texcount $thesis_prefix.tex chapter0.tex chapter1.tex chapter2.tex chapter3.tex chapter4.tex chapter5.tex chapter6.tex chapter7.tex chapter8.tex chapter9.tex chapterZ.tex | grep ^Words\ in\ headers:)"
wrdsInT="$(texcount $thesis_prefix.tex chapter0.tex chapter1.tex chapter2.tex chapter3.tex chapter4.tex chapter5.tex chapter6.tex chapter7.tex chapter8.tex chapter9.tex chapterZ.tex | grep ^Words\ in\ text:)"

python updateProgressMetrics.py "$pgsIn" "$wrdsInH" "$wrdsInT"

python postToPlotly.py
