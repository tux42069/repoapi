import requests

#response = requests.get('https://httpbin.org/ip')

data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', data=data)

print(response.json())