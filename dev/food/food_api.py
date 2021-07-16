import requests
import json
import random
import os
import datetime



def openfoodfacts_codes_extractor():
    '''Extracts the codes from the 22G DB JSON'''
    ip = "C:\\Users\drewg\Desktop\jobs\mobkoi\openfoodfacts-products.jsonl\openfoodfacts-products.json"
    with open(ip, encoding='cp437') as fp, open('codes.txt', 'w') as ofp:
        q= '\"code\":\"'
        for p, line in enumerate(fp):
            code=line.split(q, 1)[1].split('\"')[0]
            ofp.write(code+'\n')



def openfoodfacts_codes():
    with open(r"C:\Users\drewg\Desktop\jobs\mobkoi\openfoodfacts-products.jsonl\codes.txt") as fp:
        i = 1860044
        code_indexes = random.sample(range(1,i), 2) # 300 samples for 5MB
        codes = []
        for p, line in enumerate(fp):
            if p in code_indexes:
                codes.append(line.rstrip("\n"))
        return (codes)


def openfoodfacts(session, code):
    r = requests.get( 
        url =  "https://world.openfoodfacts.org/api/v0/product/" 
        + code + ".json"
    )
    # print(r.text)
    with open(session + '\\' + code + '-food'+ '.json', 'w') as fp:
        json.dump(r.json(), fp,  indent=4)



def openfoodfacts_loop():
    sessions =  "C:\\Users\drewg\Desktop\jobs\mobkoi\openfoodfacts-products.jsonl"
    session = sessions + '\\' + datetime.datetime.now().strftime("%Y%m%d_%H%M") + '_FOOD'
    print(session)
    if os.path.exists(session):
        print (session + ' already exist, aborting creation')
    else:
        os.mkdir(session)
        for code in openfoodfacts_codes():
            openfoodfacts(session, code)



def main():
    # openfoodfacts()
    # openfoodfacts_codes()
    openfoodfacts_loop()
    # openfoodfacts_codes_extractor()

if __name__ == '__main__':
    main()