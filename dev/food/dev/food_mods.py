import requests
import json
import random
import os
import datetime
import re

code = '8714368008838'

'''
openfoodfacts(8714368008838)

'''

def openfoodfacts(code):
    r = requests.get( 
        url =  "https://world.openfoodfacts.org/api/v0/product/" 
        + code + ".json"
    )

    # print(r.text)
    return (r.json())

def modify_json(sessions):
    ''''''

    j = openfoodfacts('00853484')
    ps = json.dumps(j) # product string from json
    # print(ps)

    # pattern = re.compile(r'(?<=\")(\w*-\w*)*(?=\":)') # finds all keys that have a dash * removed
    pattern = re.compile(r'(?<=\")(\w*-\w*)(?=\":)') # finds all keys that have a dash
    match = pattern.search(ps)
    print(match)
    while match is not None:
        new_str = match.group().replace('-', '_')
        ps = ps[:match.start()] + new_str + ps[match.end():]
        match = pattern.search(ps)
        print(match)

    pattern = re.compile(r'(?<=\")(\w*:\w*)(?=\":)') # finds all keys that have a dash
    match = pattern.search(ps)
    while match is not None:
        new_str = match.group().replace(':', '_')
        ps = ps[:match.start()] + new_str + ps[match.end():]
        match = pattern.search(ps)
        print(match)


    pattern = re.compile(r'(?<=\")\d\w*(?=\":)') # finds all keys that start with a number
    match = pattern.search(ps)
    while match is not None:
        new_str = '_' + match.group()
        ps = ps[:match.start()] + new_str + ps[match.end():]
        match = pattern.search(ps)
        print(match)

    ps = ps.replace('{}', '[]')

    # print(ps)

    return(json.loads(ps))

def per_product_jsonl(sessions):
    code = product_codes()[0]
    x = '{}\\{}-food.json'.format(sessions, code)

    with open(x, 'w') as fp:
        json.dump(openfoodfacts(code), fp,  indent=4)


def main():
    sessions =  "C:\\Users\\drewg\\Documents\\code\\gcp_data_pipeline\\dev\\tests"
    # product_jsonl(sessions)
    modify_json(sessions)
    # slice_str()




if __name__ == '__main__':
    main()


    '''
    Issue with keys having dash instead of underscore.
    Need to correct dashes but easier to debug with a single product json.

    Test setup and 
    1. DONE Create single product json, indent to see all keys
    ^ useful if manual schema necessary

    2. DONE Create single product json, single line to pass jsonL into bq
    - test
    3. replace("org-database-usda","org_database_usda") or manually
    - test
    4. better logic, find all keys in file, and cover all dashes - into underscores _
    - test
  
    5. NEW 400 KEY error.

    find way to query all keys in json object

    ----



    Invalid field name "org-database-usda". Fields must contain only letters, numbers, and underscores, start with a letter or underscore, and be at most 300 characters long. Table: test_food_705b4148_61db_438d_bce3_17a453ff7166_source
    
    Invalid field name "400". Fields must contain only letters, numbers, and underscores, start with a letter or underscore, and be at most 300 characters long. Table: 20210717_1803_food_86928453_b249_4352_b203_9d10969ea70b_source
    
    
    todo
    for key in product_info_keys:
        if key ==  start with a number:
            add _ at start
        if - in key:
            replace - with _
    
    
    ''' 