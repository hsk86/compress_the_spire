# Compress the spire

## Background

The largest trove of Slay the Spire (STS) runs data in existence (~77m Slay the Spire runs, ~360GB uncompressed) was recently made public.

Simply reading and parsing the data alone on a single computer is a challenge, let alone calculate complex metrics or develop machine learning models on top of this data. Cloud is a good solution for this, but at this volume of data, cost is a serious concern, especially for individual contributors to bear. A naive approach to compressing the data into Apache Parquet format resulted in ~90% compression rate; far more palatable for 

## So what does this repo do?

It does a few things:

1. :shell: Provide a couple of bash scripts that clean the data.
2. :snake: Python scripts that parses JSON files into Parquet format with Snappy compression.
3. :page_facing_up: Some documentation/guidelines around data quality.

## Parquet sounds great. What do I do with this?

Parquet used to be a purely Hadoop/HDFS file format, but it's now widely used in data warehouses and schema-on-read solutions!

- :cloud: Load into S3, thrn run SQL queries directly on the files via Athena *(personally tested, verified)*
    - Billed at $5/GB data *scanned*. Keep an eye on your AWS bill.
    - This is my personal recommendation without a beast rig at home, as long as you're not hammering it dumb queries 24/7 your bill won't amount to much. 
- :cloud: Load into Google BigQuery
    - Billed at $5/GB data *scanned*. Keep an eye on your GCP bill.
    - *Should* be as good, if not better than Athena, but don't know enough about BigQuery to make a call.
- :cloud: Load into Snowflake ($$$) 
    - Snowflake by far has the greatest performance of all data warehouses but is extremely expensive. **You have been warned. Careless home use will probably send you bankrupt. Try on a demo account without submitting your CC info to be safe.**
- :cloud: Load into Redshift
    - Not recommended, Redshift does not currently support complex data types (e.g. nested arrays/structs). You could however keep data in Amazon S3 and leverage Amazon Redshift Spectrum...but at that point why not just use Athena?
- :computer: Try running a [Clickhouse](https://clickhouse.tech/) cluster *(personally tested, verified)*. Your PC needs to be sufficiently beefy (think >64GB ram) to handle complex queries on this. Setting it up also isn't the most pleasant experience atm.
- :computer: Use it on your own Hadoop/Spark cluster, if you're into running your own clusters.