#!/bin/bash
# script to push to server  -jbsilva
source params_thesis.bash

scp $thesis_prefix.pdf $username@$save_server:$save_dir/$thesis_prefix.pdf
scp $thesis_prefix.zip $username@$save_server:$save_dir/$thesis_prefix.zip


