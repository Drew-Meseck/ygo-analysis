import bs4
import pandas as pd
import requests
import json

BASE_PATH = 'https://ygoprodeck.com/api/tournament/getTournaments.php?&_=1696097911731'


def get_resp(url, headers):
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_tournaments():
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'Cookie': 'serviceworkercacheexpire=serviceworkercacheexpire; PHPSESSID=b3e8556d52ae2f6f72c76e93a739a90c; cf_clearance=Sf4SCh38uIupA3BMA1mxIgSetsDPVSzSlnRqZIGh510-1696097468-0-1-f4809ac8.8e450513.ac16c863-0.2.1696097468',        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    print("Fetching Tournaments")
    resp = get_resp(BASE_PATH, headers)
    return resp['data']
    

def get_tops(req):
    pass

def get_lists(req):
    pass