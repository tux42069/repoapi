import requests

params = {'key1': 'horse1', 'key2': 'lizard1'}
response = requests.get('https://httpbin.org/get', params=params)

print(response.url)
print(response.json())