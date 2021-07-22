import requests
import time
'''
Run this script daily to call the 2 APIs, store in GCS, and import import into BigQuery tables

Here are the URLs to trigger the cloud functions. Included in the import functions is are example parameters.

https://us-central1-drewcollins-project-1.cloudfunctions.net/covid_api_to_gcs
https://us-central1-drewcollins-project-1.cloudfunctions.net/covid_gcs_to_bq?blob_name=20210716_2219_covid_blob

https://us-central1-drewcollins-project-1.cloudfunctions.net/food_api_to_gcs
https://us-central1-drewcollins-project-1.cloudfunctions.net/food_gcs_to_bq?blob_name=20210722_1805_food_blob
'''

def covid_pipeline():
    r = requests.get( 
        url =  "https://us-central1-drewcollins-project-1.cloudfunctions.net/covid_api_to_gcs"
    )
    covid_api_result = r.text
    print(covid_api_result)
    print('sleep for 5 before import')
    time.sleep(5)
    print('starting import')
    r2 = requests.get( 
        url =  "https://us-central1-drewcollins-project-1.cloudfunctions.net/covid_gcs_to_bq",
        params={'blob_name': covid_api_result.split(' ')[0]}
    )
    covid_bq_result = r2.text
    print(covid_bq_result)
    return

def food_pipeline():
    r = requests.get( 
        url =  "https://us-central1-drewcollins-project-1.cloudfunctions.net/food_api_to_gcs"
    )
    food_api_result = r.text
    print(food_api_result)
    print('sleep for 5 before import')
    time.sleep(5)
    print('starting import')
    r2 = requests.get( 
        url =  "https://us-central1-drewcollins-project-1.cloudfunctions.net/food_gcs_to_bq",
        params={'blob_name': food_api_result.split(' ')[0]}
    )
    food_bq_result = r2.text
    print(food_bq_result)
    return

def main():
    covid_pipeline()
    food_pipeline()


if __name__ == '__main__':
    main()