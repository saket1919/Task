import requests

url = 'https://rickandmortyapi.com/api/'

endpoint = "character"

s = requests.get(url + endpoint)

data = s.json()
pages = data['info']['pages']
print(data['results'][0])
