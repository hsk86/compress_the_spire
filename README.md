# Compress the spire

## Background

The largest trove of Slay the Spire (STS) runs data in existence (~77m Slay the Spire runs, ~360GB uncompressed) was recently made public.

Simply reading and parsing the data alone on a single computer is a challenge, let alone calculate complex metrics or develop machine learning models on top of this data. Cloud is a good solution for this, but at this volume of data, cost is a serious concern, especially for individual contributors to bear.

## So what does this repo do?

This repo provides tools and guidelines on compressing ~360GB of raw JSON logs into ~28GB parquet files for speedier processing and integration with big data tools.

:shell: Shell scripts that pre-process the data.  
:snake: Python scripts that parses JSON files into Parquet format with Snappy compression.  
:page_facing_up: Some documentation/guidelines around data quality.

## Pre-process?

If you want to run this yourself, you will almost certainly need to run some pre-processing of the raw data.

1. A couple of corrupted logs need to be fixed, otherwise it can mess with your processing (schema-on-read engines such as Spark/Presto is especially sensitive to this). See `Known Corrupted Logs` section for details.
2. Logs will present numbers in integer format (e.g. 5) in some logs, but in double format (e.g. 5.0) in others. This will create inconsistencies in your parquet schemas which can cause many systems to chuck a fit. 

## Instructions

Requirements:
- Linux or Mac, Windows will need to run within WSL
- Python 3.8+

### Clean-up corrupted logs

You *should* remove these in your copy of the raw logs before proceeding:

| File       | Issue           | Recommended Action  |
| ------------- |:-------------:| -----:|
| 2020-10-29-21-45#1250.json | Corrupt field named "s\"" | Search and remove |
| 2018-12-14-08-19#1512.json | Corrupt field named "not_p?cked" | Search and remove |  

### Clone repository

```
git clone https://github.com/hsk86/compress_the_spire.git
```

### Create and activate Virtual Environment

```
python3 -m venv <path/where/you/cloned/the/repo/env
source /path/where/you/cloned/the/repo/env/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run bash script to convert doubles to integers

```
# Remember to adjust your folder paths in the .sh script!
cd /path/where/you/cloned/the/repo
chmod +x ./scripts/replace_decimals.sh
./scripts/replace_decimals.sh
```

### Run script!

```
# Remember to adjust your folder paths in the .sh script!
cd /path/where/you/cloned/the/repo
chmod +x ./scripts/run.sh
./scripts/run.sh
```
  
## Ok, I want to run some analysis on the files. What now?

Parquet used to be a purely Hadoop/HDFS storage format, but it's now widely used in data warehouses and schema-on-read tools!

:white_check_mark: <- indicates tested and verified that it works with the outputs  
:moneybag: <- indicates using the service will cost you money. More emojis = more expensive

- :snake: Use either [pyarrow](https://arrow.apache.org/docs/python/) and/or [pandas](https://pandas.pydata.org/) packages to read parquet files into pandas DataFrames.
- :cloud: Load into Amazon S3, thrn run SQL queries directly on the files via [Amazon Athena](https://aws.amazon.com/athena/) :white_check_mark: :moneybag:
    - Billed at $5/GB data *scanned*. Keep an eye on your AWS bill.
    - This is my personal recommendation without a beast rig at home, as long as you're not hammering it with dumb queries 24/7 your bill won't amount to much. 
- :cloud: Load into [Google BigQuery](https://cloud.google.com/bigquery) :moneybag:
    - Billed at $5/GB data *scanned*. Keep an eye on your GCP bill.
    - *Should* be as good, if not better than Athena, but I don't know enough about BigQuery to make a call on this.
- :cloud: Load into [Snowflake](https://www.snowflake.com/) :moneybag::moneybag::moneybag:
    - Highly performant but is extremely **expensive**. 
        - You have been warned. Careless home use will probably **make you bankrupt**. Try on a demo account without submitting your CC info to be safe.
- :cloud: Load into [Redshift](https://aws.amazon.com/redshift/)
    - Not recommended, Redshift does not currently support complex data types (e.g. nested arrays/structs). You could however keep data in Amazon S3 and leverage Amazon Redshift Spectrum...but at that point why not just use Athena?
- :computer: Try running a [Clickhouse](https://clickhouse.tech/) data warehouse cluster on your PC or your favourite VM :white_check_mark:
    - Your PC needs to be sufficiently beefy (think >64GB ram) to handle complex queries on this.
- :computer: Use it on your own Hadoop/Spark cluster, if you're into running your own clusters.