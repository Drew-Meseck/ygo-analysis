import bs4 as bs
import pandas as pd
import requests
import json


BASE_PATH = 'https://ygoprodeck.com/api/tournament/getTournaments.php?&_=1696097911731'
TOURNAMENT_PATH = 'https://ygoprodeck.com/tournament/'
HEADERS = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'Cookie': 'serviceworkercacheexpire=serviceworkercacheexpire; PHPSESSID=b3e8556d52ae2f6f72c76e93a739a90c; cf_clearance=Sf4SCh38uIupA3BMA1mxIgSetsDPVSzSlnRqZIGh510-1696097468-0-1-f4809ac8.8e450513.ac16c863-0.2.1696097468',        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }


def get_resp(url, headers):
    resp = requests.get(url, headers=HEADERS)
    return resp.json()

def get_tournaments():
    

    print("Fetching Tournaments")
    resp = get_resp(BASE_PATH, HEADERS)
    return resp['data']
    

def get_tops():
    tournaments = pd.read_csv('src/data/tournaments.csv')
    slugs_df = tournaments[['id', 'slug']]
    test_slug = slugs_df.slug[29]
    resp = requests.get(f'{TOURNAMENT_PATH}{test_slug}', headers=HEADERS)
    soup = bs.BeautifulSoup(resp.text, features='lxml')
    tables =  soup.findAll('div', {'id': 'tournament_table'})
    tops = parse_tops(list(tables)[0], slugs_df.id[29], slugs_df.slug[29])

    return tops

def parse_tops(div, id, slug):
    rows = []
    tags_count = 0 #used to index the header as well as assign placements!
    for child in div.children: #loop through rows
        if type(child) == bs.element.Tag:
            row = {}
            #child.attrs contains refrence to deck link
            if tags_count == 0: #the first tag should always be the header, we dont need the header because we will be using a slightly different format
                tags_count += 1
                continue
            else:
                if 'href' in child.attrs.keys():
                    href = child.attrs['href']
                    #print(href)
                else:
                    href = None
                    #print(None)
            index = 0
            for c in child.children: # Get other rows in [Rank, Country, Duelist, Archetype, Sub-Archetype1, Sub-Archetype2, Price]
                if type(c) == bs.element.Tag:
                    if index == 0: #Get the Rank
                        #print(c.text)
                        rank = c.text
                    if index == 1: # Get the Country and Duelist
                        text_list = c.text.split('\n')
                        text_list = list(filter(None, text_list))
                        country = text_list[0]
                        duelist = text_list[1]
                    if index == 2:# Get the Archetypes (This is multiple children, only the first one has text, the rest are in the title of the the img tag (secondary and tirtiary))
                        for i in c.children:
                            pass
                    if index == 3:# Get the Price
                        price = c.text.replace('\n','')
                
                    index += 1
    
            row = {'id': id, 'slug': slug, 'href': href, 'rank': rank, 'country': country, 'duelist': duelist, 'archetype': '', 'sub-archetype1': '', 'sub-archetype2' : '', 'price': price}
            rows.append(row)
                        
    
    return rows


def get_lists(req):
    pass




