import requests


def main(list_superhero, URL):
    list_superhero_id = give_id(list_superhero, URL)
    name_favorite = smartest(list_superhero_id, URL)
    return name_favorite


def give_id(list_superhero, URL):
    list_id = list()
    for superhero_name in list_superhero:
        resp = requests.get(URL + 'search/' + superhero_name)
        if resp.status_code != 200:
            raise Exception('Код ответа не 200')
        for parametric in resp.json()['results']:
            if parametric['name'] == superhero_name:
                ID = parametric['id']
        list_id.append(ID)
    return list_id


def smartest(list_superhero_id, URL):
    intelligence_dict = dict()
    for id_superhero in list_superhero_id:
        resp = requests.get(URL + id_superhero + '/powerstats')
        intelligence_dict[resp.json()['name']] = int(resp.json()['intelligence'])
    intelligence_favorite = 0
    for name, intelligence in intelligence_dict.items():
        if intelligence > intelligence_favorite:
            intelligence_favorite = intelligence
            name_favorite_superhero = name
    return name_favorite_superhero


print(main(['Hulk', 'Captain America', 'Thanos'], 'https://www.superheroapi.com/api.php/2619421814940190/'))





