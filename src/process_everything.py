from json import load
import os
import fire
import logging
from os import listdir, system, getpid
from os.path import isfile, join, exists
import pandas as pd
import pyarrow
from sts_helpers import extract_year, extract_month

pd.options.mode.chained_assignment = None

def extract_json(f):
    with open(f, encoding='utf-8-sig') as json_file:
        run_logs = load(json_file)
        run_logs = [log['event'] for log in run_logs]
    return(run_logs)


def main(input_path, output_path, logfile):
    logging.basicConfig(
        filename=logfile, 
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    logging.info("Running on path {}".format(input_path))

    n_chunk = 20
    file_list_all = sorted([join(input_path, f) for f in listdir(input_path) if isfile(join(input_path, f))])
    file_list = [file_list_all[x:x+n_chunk] for x in range(0, len(file_list_all), n_chunk)]

    logging.info("Number of chunkeroos: {}. Expected files: {}".format(len(file_list), len(file_list_all)))

    for f_chunk in file_list:
        logging.info("Doing chunk, first file: {}".format(f_chunk[0]))
        chunk_logs = [extract_json(f) for f in f_chunk]
        chunk_logs = [i for sublist in chunk_logs for i in sublist]
        df = pd.DataFrame.from_dict(chunk_logs)

        ### TODO: change this
        file_year = extract_year(f_chunk[0])
        file_month = extract_month(f_chunk[0])

        output_path_y = join(output_path, file_year)
        if exists(output_path_y) is False:
            os.mkdir(output_path_y)
        
        output_path_ym = join(output_path_y, file_month)
        if exists(output_path_ym) is False:
            os.mkdir(output_path_ym)

        df.to_parquet(
            f_chunk[0].replace(input_path, output_path_ym).replace('.json', '_runs.snappy.parquet')
            ,compression='snappy'
            ,engine='pyarrow'
            ,index=False
        )
        logging.info("Great success!: {}".format(f_chunk[0]))


if __name__ == "__main__":
    fire.Fire(main)