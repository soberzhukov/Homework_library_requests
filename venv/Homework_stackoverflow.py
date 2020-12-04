import requests
from pprint import pprint

def title_of_python(url):
    resp = requests.get(url, params={'fromdate':1606953600, 'todate':1607126400, 'site':'stackoverflow'})
    resp.raise_for_status()
    items = resp.json()['items']
    for item in items:
        if 'python' in item['tags']:
            print(item['title'])

title_of_python('https://api.stackexchange.com/2.2/questions')