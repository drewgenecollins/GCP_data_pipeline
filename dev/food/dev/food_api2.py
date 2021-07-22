import requests
import json
import random
import os
import datetime
import re
import multiprocessing
import time
import ast

# def per_product_jsonl(sessions):
#     code = product_codes()[0]
#     x = '{}\\{}-food.json'.format(sessions, code)

#     with open(x, 'w') as fp:
#         json.dump(openfoodfacts(code), fp,  indent=4)

# def food_loop_many_jsons(sessions):
#     session = sessions + '\\' + datetime.datetime.now().strftime("%Y%m%d_%H%M") + '_FOOD'
#     print(session)
#     if os.path.exists(session):
#         print (session + ' already exist, aborting creation')
#     else:
#         os.mkdir(session)
#         for code in openfoodfacts_codes():
#             openfoodfacts(session, code)

# def timed_search(pattern, text):
#     return pattern.search(text)

# def modify_json2(input_json, output_json):
#     '''corrects format of JSON keys for big query import '''

#     ps = json.dumps(input_json) # product string from json

#     pattern = re.compile(r'(?<=\")(\w+[-|:]\w+)+(?=\":)') # finds all keys that have a dash
#     match = timed_search(pattern, ps)
#     print(match)
#     while match is not None:
#         new_str = match.group().replace('-', '_')
#         new_str = new_str.replace(':', '_')
#         print(new_str)
#         ps = ps[:match.start()] + new_str + ps[match.end():]
#         match = timed_search(pattern, ps)
#         print(match)
 

#     pattern = re.compile(r'(?<=\")\d\w*(?=\":)') # finds all keys that start with a number
#     match = pattern.search(ps)
#     while match is not None:
#         # print(match)
#         new_str = '_' + match.group()
#         ps = ps[:match.start()] + new_str + ps[match.end():]
#         match = pattern.search(ps)

 

#     ps = ps.replace('{}', '[]')

#     output_json.value = json.loads(ps)
#     return()

# def openfoodfacts_codes_extractor():
#     '''Extracts the codes from the 22G DB JSON'''
#     ip = r"C:\Users\drewg\Desktop\jobs\mobkoi\openfoodfacts-products.jsonl\openfoodfacts-products.json"
#     with open(ip, encoding='cp437') as fp, open('codes.txt', 'w') as ofp:
#         q= '\"code\":\"'
#         for p, line in enumerate(fp):
#             code=line.split(q, 1)[1].split('\"')[0]
#             ofp.write(code+'\n')



def product_codes(sample_size):
    with open(r"C:\Users\drewg\Documents\code\gcp_data_pipeline\dev\food\codes.txt") as fp:
        i = 1860044
        code_indexes = random.sample(range(1,i), sample_size) # 300 samples for 5MB
        codes = []
        for p, line in enumerate(fp):
            if p in code_indexes:
                codes.append(line.rstrip("\n"))
    return (codes)


def openfoodfacts(code):
    '''calls api and gives json'''
    r = requests.get( 
        url =  "https://world.openfoodfacts.org/api/v0/product/" 
        + code + ".json"
    )
    return (r.json())


# def modify_json(input_json):
def modify_json(input_json, output_dict):
    '''corrects format of JSON keys for big query import '''

    ps = json.dumps(input_json) # product string from json

    pattern = re.compile(r'(?<=\")(\w*-\w*)+(?=\":)') # finds all keys that have a dash
    match = pattern.search(ps)
    # match = timed_search(pattern, ps)
    while match is not None:
        # print(match)
        new_str = match.group().replace('-', '_')
        ps = ps[:match.start()] + new_str + ps[match.end():]
        # match = timed_search(pattern, ps)
        match = pattern.search(ps)

    pattern = re.compile(r'(?<=\")(\w*:\w*)+(?=\":)') # finds all keys that have a dash
    match = pattern.search(ps)
    while match is not None:
        # print(match)
        new_str = match.group().replace(':', '_')
        ps = ps[:match.start()] + new_str + ps[match.end():]
        match = pattern.search(ps)

    pattern = re.compile(r'(?<=\")\d\w*(?=\":)') # finds all keys that start with a number
    match = pattern.search(ps)
    while match is not None:
        # print(match)
        new_str = '_' + match.group()
        ps = ps[:match.start()] + new_str + ps[match.end():]
        match = pattern.search(ps)

    ps = ps.replace('{}', '[]')

    # output_json = json.loads(ps)
    # return()
    
    # return(json.loads(ps))
    print(ps)
    output_dict = ast.literal_eval(ps)
    # print(output_json)
    return()
    



def multi_product_jsonl(sessions):
    
    f = sessions + '\\' + datetime.datetime.now().strftime("%Y%m%d_%H%M") + '_food.jsonl'
    print(f)

    with open(f, 'w') as fp:
        for i, code in enumerate(product_codes(5)):
            print('{} code {}'.format(i, code))
            j = openfoodfacts(code) # call api with code and gives json now dict
            # m = modify_json(j)      # corrects format of JSON keys for big query import

            # -- modification timer
            # # output_json = multiprocessing.Value("dict", 0.0, lock=False)
            output_dict = multiprocessing.Manager().dict()

            p = multiprocessing.Process(target=modify_json, args= [j, output_dict])
            p.start()
            # Wait for 10 seconds or until process finishes
            p.join(5)
            if p.is_alive():
                print("modification timed out")
                p.terminate()
                p.join()
                continue
            # --

            print(output_dict)
            json.dump(output_dict, fp)
            # json.dump(output_json.value, fp)
            # json.dump(output_json, fp)

            fp.write('\n')

    return(f)


def curly():
    text = 'asdf asdd {} qa'
    text = text.replace('{}', '[]')
    print(text)

def main():
    sessions =  "C:\\Users\\drewg\\Documents\\code\\gcp_data_pipeline\\dev\\tests"
    # openfoodfacts_codes_extractor()
    # openfoodfacts()
    # per_product_jsonl(sessions)
    # openfoodfacts_codes()
    multi_product_jsonl(sessions)
    # curly()



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
    
    Invalid field name "ciqual_food_code:en". Fields must contain only letters, numbers, and underscores, start with a letter or underscore, and be at most 300 characters long. Table: 20210718_1732_food_0470cb86_3c79_408a_9f70_f78478881e65_source
    
    Unsupported empty struct type for field 'product.category_properties'


    failed at 00853484
    '''