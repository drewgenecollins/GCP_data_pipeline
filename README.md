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

1. Daily, HTTP call to cloud functions covid_api_to_gcs and food_api_to_gcs

2. Fill out blob names and HTTP call cloud functions covid_gcs_to_bq and food_gcs_to_bq

## todo

### call API request for data

### Write file data to bucket

need authentication to access bucket

https://googleapis.dev/python/storage/latest/index.html

https://cloud.google.com/functions/docs/concepts/exec#functions-concepts-stateless-python

https://cloud.google.com/appengine/docs/standard/python/googlecloudstorageclient/read-write-to-cloud-storage

https://cloud.google.com/functions/docs/writing/http#uploading_files_via_cloud_storage

access bucket from cloud functions

https://pythonexamples.org/python-requests-http-put/

gcloud projects add-iam-policy-binding drewcollins-project-1 --member serviceAccount:account-1@drewcollins-project-1.iam.gserviceaccount.com --role roles/iam.serviceAccountTokenCreator

changed the service account listed for function-3

https://us-central1-drewcollins-project-1.cloudfunctions.net/function-5

cloud function now writes covid data to blucket blob

## import data into bigquery

if want to get fancy
https://cloud.google.com/functions/docs/calling/storage

### create cloud function arg for api key

add agrs for cloud function

