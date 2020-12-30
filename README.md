# Compress the spire

## Background

The largest trove of Slay the Spire (STS) runs data in existence (~77m Slay the Spire runs, ~360GB uncompressed) was recently made public.

Simply reading and parsing the data alone on a single computer is a challenge, let alone calculate complex metrics or develop machine learning models on top of this data. Cloud is a good solution for this, but at this volume of data, cost is a serious concern, especially for individual contributors to bear.

## So what does this repo do?

This repo provides tools and guidelines on compressing ~360GB of raw JSON logs into ~28GB parquet files.

1. :shell: Provide a couple of bash scripts that pre-process the data.
2. :snake: Python scripts that parses JSON files into Parquet format with Snappy compression.
3. :page_facing_up: Some documentation/guidelines around data quality.

## Pre-process?

If you want to run this yourself, you will almost certainly need to run some pre-processing of the raw data.

1. A couple of corrupted logs need to be fixed, otherwise it can mess with your processing (schema-on-read engines such as Spark/Presto is especially sensitive to this).
2. Logs will present numbers in integer format (e.g. 5) in some logs, but in double format (e.g. 5.0) in others. This will create inconsistencies in your parquet schemas which can cause many systems to chuck a fit. 

## Parquet sounds great. What do I do with this?

Parquet used to be a purely Hadoop/HDFS storage format, but it's now widely used in data warehouses and schema-on-read tools!

:white_check_mark: <- indicates tested and verified that it works with the outputs  
:moneybag: <- indicates using the service will cost you money. More emojis = more expensive

- :snake: Use either [pyarrow](https://arrow.apache.org/docs/python/) and/or [pandas](https://pandas.pydata.org/) packages to read parquet files into pandas DataFrames.
- :cloud: Load into Amazon S3, thrn run SQL queries directly on the files via [Amazon Athena](https://aws.amazon.com/athena/) :white_check_mark: :moneybag:
    - Billed at $5/GB data *scanned*. Keep an eye on your AWS bill.
    - This is my personal recommendation without a beast rig at home, as long as you're not hammering it dumb queries 24/7 your bill won't amount to much. 
- :cloud: Load into [Google BigQuery](https://cloud.google.com/bigquery) :moneybag:
    - Billed at $5/GB data *scanned*. Keep an eye on your GCP bill.
    - *Should* be as good, if not better than Athena, but I don't know enough about BigQuery to make a call on this.
- :cloud: Load into [Snowflake](https://www.snowflake.com/) :moneybag::moneybag::moneybag:
    - Highly performant but is extremely **expensive**. 
        - You have been warned. Careless home use will probably **make you bankrupt**. Try on a demo account without submitting your CC info to be safe.
- :cloud: Load into Redshift
    - Not recommended, Redshift does not currently support complex data types (e.g. nested arrays/structs). You could however keep data in Amazon S3 and leverage Amazon Redshift Spectrum...but at that point why not just use Athena?
- :computer: Try running a [Clickhouse](https://clickhouse.tech/) data warehouse cluster on your PC or your favourite VM :white_check_mark:
    - Your PC needs to be sufficiently beefy (think >64GB ram) to handle complex queries on this.
- :computer: Use it on your own Hadoop/Spark cluster, if you're into running your own clusters.