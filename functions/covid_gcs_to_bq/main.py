from google.cloud import bigquery


def covid_gcs_to_bq(request):
    # pip install --upgrade google-cloud-bigquery
    
    blob_name = request.args.get('blob_name')
    # blob_name = '20210716_1136_covid_blob'
    
    client = bigquery.Client()

    table_id = '{}.{}.{}_table'.format(
        'drewcollins-project-1',
        'covid',
        blob_name
    )
    job_config = bigquery.LoadJobConfig(
        autodetect=True, source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    )
    uri = "gs://bucket-1-7233/" + blob_name
    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.
    load_job.result()  # Waits for the job to complete.
    destination_table = client.get_table(table_id)

    return "Loaded {} rows into {}".format(destination_table.num_rows, table_id)