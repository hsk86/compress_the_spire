#!/bin/bash
set -euo

# Here raw files have been partitioned into 8 sub-folders so that the scripts can be run in parallel. 
# Adjust the number of subfolders depending on your ability to parallelise on your system.

PATTERN='s/\.0//g'
RAW_FILE_ROOT_FOLDER=/path/to/raw/sts/logs

find $RAW_FILE_ROOT_FOLDER/0/. -type f -exec sed -i -e $PATTERN {} \; &
find $RAW_FILE_ROOT_FOLDER/1/. -type f -exec sed -i -e $PATTERN {} \; &
find $RAW_FILE_ROOT_FOLDER/2/. -type f -exec sed -i -e $PATTERN {} \; &
find $RAW_FILE_ROOT_FOLDER/3/. -type f -exec sed -i -e $PATTERN {} \; &
find $RAW_FILE_ROOT_FOLDER/4/. -type f -exec sed -i -e $PATTERN {} \; &
find $RAW_FILE_ROOT_FOLDER/5/. -type f -exec sed -i -e $PATTERN {} \; &
find $RAW_FILE_ROOT_FOLDER/6/. -type f -exec sed -i -e $PATTERN {} \; &
find $RAW_FILE_ROOT_FOLDER/7/. -type f -exec sed -i -e $PATTERN {} \; &