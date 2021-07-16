import requests
import datetime
import subprocess
import json

# Imports the Google Cloud client library
from google.cloud import storage


def covid_api():

    '''
    1.384MB JSON data ingestion
    https://rapidapi.com/KishCom/api/covid-19-coronavirus-statistics/
    '''
    r = requests.get( 
        url =  "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats",
        headers={
        'x-rapidapi-key': "xx",
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
        }
    )
    with open(datetime.datetime.now().strftime("%Y%m%d_%H%M") + '_covid_data.json', 'w') as fp:
    #     json.dump(r.json(), fp,  indent=4)
        json.dump(r.json(), fp) # bigquery requires JSONL format
    return(print(r.json()))


def write_to_bucket():

    bucket = storage.Client().bucket('bucket-1-7233')
    blob = bucket.blob('storage_blob_2')
    with blob.open('w') as f:
        f.write('Hello world\n123')

def covid_api_write_to_bucket():
    r = requests.get( 
        url =  "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats",
        headers={
        'x-rapidapi-key': "xx",
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
        }
    )

    t= datetime.datetime.now().strftime("%Y%m%d_%H%M")
    
    bucket = storage.Client().bucket('bucket-1-7233')
    blob = bucket.blob(t + '_covid_blob')

    with blob.open('w') as f:
        json.dump(r.json(), f,  indent=4)

    return(print(t + '_covid_blob created within bucket-1-7233' ))


def main():
    # auth()
    # covid_api_write_to_bucket()
    covid_api()

if __name__ == '__main__':
    main()


'''
1. call API request for data
2. Write file data to bucket 
'''