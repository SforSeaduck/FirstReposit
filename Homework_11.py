import requests
from pprint import pprint

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url=url)
json_file = response.json()
count_astro = json_file['number']
astronafts = json_file["people"]
# astro_name = astronafts[0]["name"]


for astro in range(0, count_astro):
    print(astronafts[astro]["name"])
