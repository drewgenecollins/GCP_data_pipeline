import requests
import json
import random
import os
import datetime
import re
import multiprocessing
import time
import ast

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

def modify_json(input_json, output_dict):
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
    # print(type(ps))
    # print(ps)
    output_dict = json.loads(ps)
    print(output_dict)
    



def multi_product_jsonl(sessions):
    
    f = sessions + '\\' + datetime.datetime.now().strftime("%Y%m%d_%H%M") + '_food.jsonl'
    print(f)

    with open(f, 'w') as fp:
        for i, code in enumerate(product_codes(5)):
            print('{} code {}'.format(i, code))

            input_json = openfoodfacts(code) # call api with code and gives json now dict
            # output_dict = multiprocessing.Manager().dict()
            queue = multiprocessing.Queue()

            # p = multiprocessing.Process(target=modify_json, args= (input_json, output_dict)
            p = multiprocessing.Process(target=modify_json, args= (input_json, queue)
            p.start()
            p.join(5)
            if p.is_alive():
                print("modification timed out")
                p.terminate()
                p.join()
                continue

            print(output_dict)
            json.dump(output_dict, fp)

            fp.write('\n')

def main():
    sessions =  "C:\\Users\\drewg\\Documents\\code\\gcp_data_pipeline\\dev\\tests"

    multi_product_jsonl(sessions)



if __name__ == '__main__':
    main()

    '''
    '''