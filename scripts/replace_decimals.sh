#!/bin/bash
set -euo

# Here raw files have been partitioned into 8 sub-folders so that the scripts can be run in parallel. 
# Adjust the number of subfolders depending on your ability to parallelise on your system.

PATTERN='s/\.0//g'
RAW_FILE_ROOT_FOLDER=/path/to/raw/sts/logs

find $RAW_FILE_ROOT_FOLDER -type f -exec sed -i -e $PATTERN {} \;