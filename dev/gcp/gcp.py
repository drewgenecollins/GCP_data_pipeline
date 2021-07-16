import subprocess
import datetime
# Imports the Google Cloud client library
from google.cloud import storage
# import google


# cd \Desktop\jobs\mobkoi\openfoodfacts-products.jsonl\GCP_data_pipeline\GCP_data_pipeline\
x= 'C:\\Users\\drewg\\Desktop\\jobs\\mobkoi\\openfoodfacts-products.jsonl\\GCP_data_pipeline\\GCP_data_pipeline\\'
cmd1= [x+'\\env\\Scripts\\activate']
# python -u gcp.py

# subprocess calls cmd shell language
def gcp():
    cmd3 = ['gcloud']
    subprocess.Popen(cmd1, shell=True)
    subprocess.Popen(cmd3, shell=True)


def upload_to_bucket():
    # Cloud Storage Client Libraries setup 
    '''
    https://cloud.google.com/storage/docs/reference/libraries#using_the_client_library
    pip install --upgrade google-cloud-storage
    gcloud info 
    Project_ID= drewcollins-project-1
    authentication setup
    gcloud iam service-accounts create account-1
    gcloud projects add-iam-policy-binding drewcollins-project-1 --member="serviceAccount:account-1@drewcollins-project-1.iam.gserviceaccount.com" --role="roles/owner"
    gcloud iam service-accounts keys create key.json --iam-account=account-1@drewcollins-project-1.iam.gserviceaccount.com
    for cmd
    set GOOGLE_APPLICATION_CREDENTIALS=C:\\Users\\drewg\\Desktop\\jobs\\mobkoi\\openfoodfacts-products.jsonl\\GCP_data_pipeline\\GCP_data_pipeline\\key.json
    '''

    # uploading objects
    # https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-code-sample
    

    pass

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

def auth():
    ''' not working from subprocess for some reason
    '''
    # set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\drewg\Desktop\jobs\mobkoi\openfoodfacts-products.jsonl\GCP_data_pipeline\GCP_data_pipeline\key.json
    cmd1= ['set', r'GOOGLE_APPLICATION_CREDENTIALS=C:\Users\drewg\Desktop\jobs\mobkoi\openfoodfacts-products.jsonl\GCP_data_pipeline\GCP_data_pipeline\key.json']
    subprocess.Popen(cmd1, shell=True)


def list_buckets():
    """Lists all buckets."""

    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

def list_bucketz():
    """Lists all buckets."""

    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    b=[]
    for bucket in buckets:
        b.append(bucket.name)

    return(print(b))

def write_to_bucket(bucket_name, destination_blob_name):

    bucket = storage.Client().bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    with blob.open('w') as f:
        f.write('Hello world\n123')

def read_from_bucket(bucket_name, destination_blob_name):
    bucket = storage.Client().bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    with blob.open('r') as f:
        print(f.read())


def main():
    # covid_api()
    # auth()
    list_bucketz()
    # upload_blob(
    #     'bucket-1-7233',
    #     r'C:\Users\drewg\Desktop\jobs\mobkoi\openfoodfacts-products.jsonl\GCP_data_pipeline\GCP_data_pipeline\example.txt',
    #     'storage_blob_1'
    #     )
    # print('Hello world\n123')
    # write_to_bucket('bucket-1-7233','storage_blob_2')
    # read_from_bucket('bucket-1-7233','20210716_0042_covid_blob')
 

if __name__ == '__main__':
    main()

