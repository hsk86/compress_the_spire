#!/bin/bash
set -euo

# Here raw files have been partitioned into 8 sub-folders so that the scripts can be run in parallel. 
# Adjust the number of subfolders depending on your ability to parallelise on your system.

INPUT_FOLDER=/path/to/raw/sts/logs
OUTPUT_FOLDER=/path/where/outputs/should/go

rm -rf $OUTPUT_FOLDER/*

python3 process_runfiles.py $INPUT_FOLDER $OUTPUT_FOLDER \ ./log_run.txt