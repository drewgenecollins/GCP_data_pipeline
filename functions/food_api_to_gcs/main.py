from google.cloud import storage
import requests
import datetime
import json
import re
# import random

def product_codes(sample_size):
    # with open("codes.txt") as fp:
    #     i = 1860044
    #     code_indexes = random.sample(range(1,i), sample_size) # 300 samples for 5MB
    #     codes = []
    #     for p, line in enumerate(fp):
    #         if p in code_indexes:
    #             codes.append(line.rstrip("\n"))
    codes = ['3348450000056', '3760155980042', '3770003502685', '8710899103806','851770006316']
    return (codes)

def openfoodfacts(code):
    '''calls api and gives json'''
    r = requests.get( 
        url =  "https://world.openfoodfacts.org/api/v0/product/" 
        + code + ".json"
    )
    return (r.json())



def modify_json(input_json):
    '''corrects format of JSON keys for big query import '''

    ps = json.dumps(input_json) # product string from json

    pattern = re.compile(r'(?<=\")(\w*-\w*)+(?=\":)') # finds all keys that have a dash
    match = pattern.search(ps)
    while match is not None:
        new_str = match.group().replace('-', '_')
        ps = ps[:match.start()] + new_str + ps[match.end():]
        match = pattern.search(ps)

    pattern = re.compile(r'(?<=\")(\w*:\w*)+(?=\":)') # finds all keys that have a dash
    match = pattern.search(ps)
    while match is not None:
        new_str = match.group().replace(':', '_')
        ps = ps[:match.start()] + new_str + ps[match.end():]
        match = pattern.search(ps)

    pattern = re.compile(r'(?<=\")\d\w*(?=\":)') # finds all keys that start with a number
    match = pattern.search(ps)
    while match is not None:
        new_str = '_' + match.group()
        ps = ps[:match.start()] + new_str + ps[match.end():]
        match = pattern.search(ps)

    ps = ps.replace('{}', '[]')

    return(json.loads(ps))





def food_api_to_gcs(request):

    t= datetime.datetime.now().strftime("%Y%m%d_%H%M")    
    bucket = storage.Client().bucket('bucket-1-7233')
    blob = bucket.blob(t + '_food_blob')

    with blob.open('w') as fp:
            for i, code in enumerate(product_codes(5)):
                print('{} code {}'.format(i, code))
                j = openfoodfacts(code) # call api with code and gives json now dict
                m = modify_json(j)      # corrects format of JSON keys for big query import
                json.dump(m, fp)
                fp.write('\n')


    return '{}_food_blob created within bucket-1-7233'.format(t)