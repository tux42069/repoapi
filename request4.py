# Import the module
import requests

# set variables
REPO_URL = 'https://httpbin.org/get'
USERNAME = 'test123'
PASSWORD = 'test123'

#image_path = '/harbor/images/debian' 
tag = '11.9'

# Loging to fake repo
login_url = f'{REPO_URL}/c/login'
response = requests.post(login_url, data={'username': USERNAME, 'password': PASSWORD})

# Creating fake data
image_data = {
    "name": "debian",
    "version": "{tag}",
    "description": "Debian-based Linux operating system."
}
# Putting data on the server
response = requests.post(REPO_URL, json=image_data)

# Recalling data on the server
response = requests.get(REPO_URL)

if response.status_code == 200:
    print(f'{image_path}:{tag} Image is present')
    print(response.json())
    # Where the image move command will go
else:
    print(f'{image_path}:{tag} Image not present')

print(f"Response status code: {response.status_code}")