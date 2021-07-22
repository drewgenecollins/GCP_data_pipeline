import requests
import json
import random
import os
import datetime
import re
import multiprocessing
import time
import ast


def modify_json(input_json, queue):
    '''corrects format of JSON keys for big query import '''

    ps = json.dumps(input_json) # product string from json

    output_dict = json.loads(ps)

    queue.put(output_dict)
    return(print('mod done'))
    



def multi_product_jsonl(sessions):
    
    f = sessions + '\\' + datetime.datetime.now().strftime("%Y%m%d_%H%M") + '_food.jsonl'
    print(f)

    with open(f, 'w') as fp:
        for i, code in enumerate(product_codes(5)):
            print('{} code {}'.format(i, code))

            input_json = openfoodfacts(code) # call api with code and gives json now dict

            queue = multiprocessing.Queue()

            p = multiprocessing.Process(target=modify_json, args= (input_json, queue))
            p.start()
            p.join(10)
            a=queue.get()
            print(a)
            json.dump(a, fp)


            # if p.is_alive():
            #     print("modification timed out")
            #     p.terminate()
            #     p.join()
            #     continue
            


            fp.write('\n')

def main():
    sessions =  "C:\\Users\\drewg\\Documents\\code\\gcp_data_pipeline\\dev\\tests"
    multi_product_jsonl(sessions)



if __name__ == '__main__':
    main()

    '''
    '''