from google.cloud import storage
import requests
import datetime
import json
import os

def covid_api_to_gcs(request):
    covid_key = os.environ.get('covid_key')
    # request.args.get('covid_key')


    r = requests.get( 
        url =  "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats",
        headers={
        'x-rapidapi-key': covid_key,
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
        }
    )

    t= datetime.datetime.now().strftime("%Y%m%d_%H%M")
    
    bucket = storage.Client().bucket('bucket-1-7233')
    blob = bucket.blob(t + '_covid_blob')

    with blob.open('w') as f:
        json.dump(r.json(), f)


    return '{}_covid_blob created within bucket-1-7233'.format(t)