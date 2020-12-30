#!/bin/bash
set -euo

# Here raw files have been partitioned into 8 sub-folders so that the scripts can be run in parallel. 
# Adjust the number of subfolders depending on your ability to parallelise on your system.

INPUT_FOLDER=/path/to/raw/sts/logs
OUTPUT_FOLDER=/path/where/outputs/should/go

source env/bin/activate
rm -rf $OUTPUT_FOLDER/*

python3 process_runfiles.py $INPUT_FOLDER/sub_folder_0 $OUTPUT_FOLDER \ ./log_run.txt &
python3 process_runfiles.py $INPUT_FOLDER/sub_folder_1 $OUTPUT_FOLDER \ ./log_run.txt &
python3 process_runfiles.py $INPUT_FOLDER/sub_folder_2 $OUTPUT_FOLDER \ ./log_run.txt &
python3 process_runfiles.py $INPUT_FOLDER/sub_folder_3 $OUTPUT_FOLDER \ ./log_run.txt &
python3 process_runfiles.py $INPUT_FOLDER/sub_folder_4 $OUTPUT_FOLDER \ ./log_run.txt &
python3 process_runfiles.py $INPUT_FOLDER/sub_folder_5 $OUTPUT_FOLDER \ ./log_run.txt &
python3 process_runfiles.py $INPUT_FOLDER/sub_folder_6 $OUTPUT_FOLDER \ ./log_run.txt &
python3 process_runfiles.py $INPUT_FOLDER/sub_folder_7 $OUTPUT_FOLDER \ ./log_run.txt &