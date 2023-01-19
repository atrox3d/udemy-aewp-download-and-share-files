from filestack import Client
from secret import filestack_apikey

client = Client(filestack_apikey.API_KEY)
link = client.upload(filepath='.gitignore')

print(link.url)

