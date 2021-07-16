import requests

def covid(self):
    '''
    1.384MB JSON data ingestion
    https://rapidapi.com/KishCom/api/covid-19-coronavirus-statistics/
    '''
    r = requests.get( 
        url =  "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats",
        headers={
        'x-rapidapi-key': "xx",
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
        }
    )
    # with open(datetime.datetime.now().strftime("%Y%m%d_%H%M") + '_covid_data.json', 'w') as fp:
    #     json.dump(r.json(), fp,  indent=4)
    return(print(r.json()))