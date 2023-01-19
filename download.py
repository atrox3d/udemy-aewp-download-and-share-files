import requests
import json

url = "https://filesamples.com/samples/audio/mp3/Symphony%20No.6%20(1st%20movement).mp3"

# try to get file size before downloading it
    # size = requests.get(url, stream=True).headers['Content-length']
    # response = requests.get(url, stream=True, headers={'Accept-Encoding': None})
response = requests.head(url)
d = dict(response.headers)
print(json.dumps(d, indent=4))
size = response.headers.get('Content-Length', 'Unknown size')
print(f'{size=}')

# download file
with requests.get(url) as response:
    content = response.content
    size = len(content)
    print(f'{size:11,} bytes')
    size = round(len(content) / 1024)
    print(f'{size:11,} kilobytes')

    with open('download.mp3', 'wb') as mp3:
        mp3.write(content)


