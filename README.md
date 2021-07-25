# GCP_data_pipeline

## Task Description

Build a simple data pipeline, using a minimum of 2 APIs from any source of your choice to run on a daily basis using cloud functions. The data needs to be stored on GCS and imported into BigQuery.
Data ingested by the API's should be minimum of 5 MB

Input - minimum of 2 API's in either CSV / JSON format.

Invocation - Cloud function to be used to call API’s (if this is not possible use compute instance)

Data store - store data in GCS (google cloud storage)

Database - store final data in BigQuery tables

## APIs selected

Covid stats https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats

Food info https://world.openfoodfacts.org/api/v0/product/

## Pipeline

Daily, call the script `gcp_data_pipeline.py`

1. Script calls 2 APIs

2. Stores data in GCS

3. Imports data into BigQuery tables

Result within 2 BQ datasets called "covid" and "food".

## about

Please reach me at drewgenecollins@gmail.com for further questions and accessing the GCP project.

## Presentation

https://docs.google.com/presentation/d/1aEcnMI2L_ljvqloekexlvzGrtKwOM4LNVW0YmKePfgI/edit?usp=sharing
