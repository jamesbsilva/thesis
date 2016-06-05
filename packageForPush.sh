#!/bin/bash
# script to package files -jbsilva
source params_thesis.bash

rm $thesis_prefix.zip
zip -r ${thesis_prefix}.zip ${thesis_prefix}.pdf ${thesis_prefix}_sm.pdf ${thesis_prefix}.tex ${thesis_prefix}.bib bu_thesis.sty chapter*.tex Figures/ Images/



