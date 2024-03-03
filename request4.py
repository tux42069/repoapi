# Import the module
import requests

# set variables
REPO_URL = 'https://httpbin.org/get'
USERNAME = 'test123'
PASSWORD = 'test123'

image_path = '/harbor/images/debian'
tag = '11.9'

# Loging to repo
login_url = f'{REPO_URL}/c/login'
response = requests.post(login_url, data={'username': USERNAME, 'password': PASSWORD})

image_data = {
    "name": "debian",
    "version": "{tag}",
    "description": "Debian-based Linux operating system."
}
response = requests.post(REPO_URL, json=image_data)
response = requests.get(REPO_URL)

if response.status_code == 200:
    print(f'{image_path}:{tag} Image is present')
    print(response.json())
else:
    print(f'{image_path}:{tag} Image not present')

print(f"Response status code: {response.status_code}")