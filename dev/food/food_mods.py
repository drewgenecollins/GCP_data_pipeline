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

def myprint(d):
    for k, v in d.items():
        if isinstance(v, dict):
            print(k)
            myprint(v)
        else:
            print("{0} : {1}".format(k, v))

def myprint_keys(d):
    for k, v in d.items():
        if isinstance(v, dict):
            myprint(v)
        else:
            print(k)

def modify_json_dict():
    '''
    "400":
    "_400":

    200
    100
    2
    1
    saturated-fat_unit

    https://realpython.com/python-json/
    https://realpython.com/python-dicts/
    https://stackoverflow.com/questions/5904969/how-to-print-a-dictionarys-key
    https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary
    https://stackoverflow.com/questions/10756427/loop-through-all-nested-dictionary-values
    '''
    j = openfoodfacts('8714368008838')

    # to get keys print all values with "":



    # dictionary[new_key] = dictionary.pop(old_key)
    # j.['_code'] = j.pop('code')

    myprint_keys(j)





    print(list(j.keys())) # only shows keys on first level

    # print(j)


def myprint_keys(d):
    for k, v in d.items():
        if isinstance(v, dict):
            myprint(v)
        else:
            print(k)

def slice_str2(text, new_str, start_index, end_index):
    # text = 'abcdefg' # replace b with z
    # text = text[:1] + 'Z' + text[2:] # replaces from index 1

    # text = '\"400\"' # replace cde with ZZZ
    # old = '400'
    # new = '_400'
    # start_index = 1
    # print(len(old))
    # end_index = start_index + len(old)

    text = text[:start_index] + new_str + text[end_index:]

    return(text)


def slice_str(text, new_str, start_index, end_index):
    # text = 'abcdefg' # replace b with z
    # text = text[:1] + 'Z' + text[2:] # replaces from index 1

    # text = '\"400\"' # replace cde with ZZZ
    # old = '400'
    # new = '_400'
    # start_index = 1
    # print(len(old))
    # end_index = start_index + len(old)

    text = text[:start_index] + new_str + text[end_index:]

    return(text)

def sub_str_find_replace(text, re_pattern, old, new):
    '''find and replace sub-sub str in sub str pattern'''


    '''    
    pattern = re.compile(r'(?<=\")(\w*-\w*)*(?=\":)') # finds all keys that have a dash
    matches = pattern.finditer(ps)
    for match in matches:
        # print(match)
        new_str = match.group().replace("-","_")

        # replace old with new in parent str
        ps = ps[:match.start()] + new_str + ps[match.end():]
    '''
    pattern = re.compile(re_pattern) # finds all keys that have a dash
    matches = pattern.finditer(text)
    for match in matches:
        # print(match)
        new_str = match.group().replace(old, new)

        # replace old with new in parent str
        text = text[:match.start()] + new_str + text[match.end():]
    # print(text)
    return(text)


def modify_json_str2():
    '''
    "400":
    "_400":

    200
    100
    2
    1
    saturated-fat_unit

    https://developers.google.com/edu/python/regular-expressions#findall
    # to get keys print all values with "":
    y = re.findall(r"(?<=AAA).*?(?=ZZZ)", str)
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
  
    '''
    j = openfoodfacts('8714368008838')
    ps = (json.dumps(j)) # product string from json
    # print(ps)

    # pattern = re.compile(r"\"\w+\":") # finds all keys
    # pattern = re.compile(r'(?<=\")\d\w*(?=\":)') # finds all keys that start with a number
    # pattern = re.compile(r'(?<=\")(\w*-\w*)*(?=\":)') # finds all keys that have a dash


    ps = sub_str_find_replace(
        ps,
        r'(?<=\")(\w*-\w*)*(?=\":)', 
        '-', 
        '_'
        )



    pattern = re.compile(r'(?<=\")\d\w*(?=\":)') # finds all keys that start with a number
    matches = pattern.finditer(ps)
    for match in matches:
        # print(match.group())
        print('match plus 2 char around ' + ps[match.start()-2:match.end()+2])
        new_str = '_' + match.group()
        print('new str ' + new_str)
        print('new str in ps with 2 on both sides' + ps[match.start() -2:match.start()] + new_str + ps[match.end():match.end()+2])
        # replace old with new in parent str
        ps = ps[:match.start()] + new_str + ps[match.end():]

    print(ps)


def modify_json_str3(sessions):
    '''issue
    {"100":
    converts to
    {_1000":
    '''

    # j = openfoodfacts('8714368008838')

    # # ----
    # # x = '{}\\{}-food-input.json'.format(sessions, '8714368008838')
    # # with open(x, 'w') as fp:
    # #     json.dump(j, fp,  indent=4)


    # ps = (json.dumps(j)) # product string from json


    x = '{}\\numb.json'.format(sessions)
    # with open(x, 'w') as fp:
    #     fp.write(ps)
    
    with open(x, 'r') as fp:
        ps = fp.read().replace('\n', '')
        print(ps)
        # pattern = re.compile(r'(?<=\")(\w*-\w*)*(?=\":)') # finds all keys that have a dash
        # matches = pattern.finditer(ps)
        # for match in matches:
        #     new_str = match.group().replace('-', '_')

        #     # replace old with new in parent str
        #     ps = ps[:match.start()] + new_str + ps[match.end():]

        # pattern = re.compile(r'(?<=\")\d\w*(?=\":)') # finds all keys that start with a number
        # matches = pattern.finditer(ps)
        # for match in matches:
        #     print(match)
        #     print('match plus 2 char around ' + ps[match.start()-2:match.end()+2])
        #     new_str = '_' + match.group()
        #     print('new str ' + new_str)
        #     print('new str in ps with 2 on both sides' + ps[match.start() -2:match.start()] + new_str + ps[match.end():match.end()+2])
        #     # replace old with new in parent str
        #     ps = ps[:match.start()] + new_str + ps[match.end():]

        # pattern = re.compile(r'(?<=\")\d\w*(?=\":)') # finds all keys that start with a number

        pattern = re.compile(r'(?<=\")\d\w*(?=\":)') # finds all keys that start with a number
        match = pattern.search(ps)

        # for x in range(20):
        while match is not None:
            print(match)
            new_str = '_' + match.group()
            ps = ps[:match.start()] + new_str + ps[match.end():]
            print(ps)
            match = pattern.search(ps)

        # # while matches is not None:
        # for x in range(2):
        #     match = next(iter(matches))
        #     new_str = '_' + match.group()
        #     ps = ps[:match.start()] + new_str + ps[match.end():]
        #     print(ps)
        #     matches = pattern.finditer(ps)
        #     print(next(iter(matches)))
            

        '''

        while any matches of pattern:
            new_str = '_' + match.group()
            ps = ps[:match.start()] + new_str + ps[match.end():]

        '''


        # print(ps)
        # x = '{}\\{}-food-output.json'.format(sessions, '8714368008838')
        # with open(x, 'w') as fp:
        #     # json.dump(json.loads(ps), fp,  indent=4)
        #     fp.write(ps)

# def str_pattern_modify(re_pattern, text, new_str):
#     pattern = re.compile(re_pattern) # finds all keys that start with a number
#     match = pattern.search(text)
#     while match is not None:
#         str_pattern_modify.old_str= match.group()
#         str_pattern_modify.a=2
#         # example: new_str = '_' + old_str
#         ps = ps[:match.start()] + new_str + ps[match.end():]
#         match = pattern.search(ps)
#     return(ps)


def modify_json_str4(sessions):

    j = openfoodfacts('8714368008838')
    ps = (json.dumps(j)) # product string from json
    print(ps)

    # # ps = str_pattern_modify(  
    # #     r'(?<=\")(\w*-\w*)*(?=\":)',
    # #     ps,
    # #     str_pattern_modify.old_str.replace('-', '_')
    # # )
    # print(str_pattern_modify.a)

    # pattern = re.compile(r'(?<=\")(\w*-\w*)*(?=\":)') # finds all keys that have a dash
    # match = pattern.search(ps)
    # while match is not None:
    #     new_str = match.group().replace('-', '_')
    #     ps = ps[:match.start()] + new_str + ps[match.end():]
    #     match = pattern.search(ps)



    # pattern = re.compile(r'(?<=\")\d\w*(?=\":)') # finds all keys that start with a number
    # match = pattern.search(ps)
    # while match is not None:
    #     new_str = '_' + match.group()
    #     ps = ps[:match.start()] + new_str + ps[match.end():]
    #     match = pattern.search(ps)


    print(ps)

def modify_json(sessions):
    ''''''

    j = openfoodfacts('8714368008838')
    ps = json.dumps(j) # product string from json

    pattern = re.compile(r'(?<=\")(\w*-\w*)*(?=\":)') # finds all keys that have a dash
    match = pattern.search(ps)
    while match is not None:
        new_str = match.group().replace('-', '_')
        ps = ps[:match.start()] + new_str + ps[match.end():]
        match = pattern.search(ps)

    pattern = re.compile(r'(?<=\")(\w*:\w*)*(?=\":)') # finds all keys that have a dash
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

    return(json.loads(ps))

def per_product_jsonl(sessions):
    code = product_codes()[0]
    x = '{}\\{}-food.json'.format(sessions, code)

    with open(x, 'w') as fp:
        json.dump(openfoodfacts(code), fp,  indent=4)


def main():
    sessions =  "C:\\Users\\drewg\\Documents\\code\\gcp_data_pipeline\\dev\\tests"
    # product_jsonl(sessions)
    modify_json_str(sessions)
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