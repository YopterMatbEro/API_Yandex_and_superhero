import requests
from pprint import pprint
import json

list_name_heroes = ['Hulk', 'Captain America', 'Thanos', 'Thor']  # for test introduced Thor

api = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
json_api = api.json()

list_heroes = sorted([[i['powerstats']['intelligence'], i['name']] for i in json_api if list_name_heroes.count(i['name'])])
print(list_heroes)
pprint(f'Самый умный герой: {list_heroes[-1][1]}, с интеллектом: {list_heroes[-1][0]}')


# url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/"
# person_intelligence = []
#
# hulk_stats = json.loads(requests.get(url + '332.json').text)
# cap_stats = json.loads(requests.get(url + '149.json').text)
# thanos_stats = json.loads(requests.get(url + '655.json').text)
#
# person_intelligence.append({'hulk': hulk_stats['intelligence']})
# person_intelligence.append({'cap': cap_stats['intelligence']})
# person_intelligence.append({'thanos': thanos_stats['intelligence']})
#
# max_int = ['name', 0]
# for i in range(len(person_intelligence)):
#     for key, value in person_intelligence[i].items():
#         if value > max_int[1]:
#             max_int = [key, value]
# print(f'Самый умный герой: {max_int[0].capitalize()}, с интеллектом: {max_int[1]}')
