from google.cloud import storage

def write_to_bucket(self):

    bucket = storage.Client().bucket('bucket-1-7233')
    blob = bucket.blob('storage_blob_2')
    with blob.open('w') as f:
        f.write('Hello world\n123')

def list_buckets(self):
    """Lists all buckets."""

    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    b=[]
    for bucket in buckets:
        b.append(bucket.name)

    return(print(b))

list_buckets(None)