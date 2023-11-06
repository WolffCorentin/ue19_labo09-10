import requests

r = requests.get(url="https://punapi.rest/api/pun")
print(r.content)