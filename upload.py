import requests

url = 'https://cgi-lib.berkeley.edu/ex/fup.cgi'

with open('.gitignore', 'rb') as file:
    with requests.post(url, files={'upfile': file}) as response:
        print(response.text)
