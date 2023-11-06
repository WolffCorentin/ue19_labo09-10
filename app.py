import requests

for i in range(1,500):
  r = requests.get(url="https://punapi.rest/api/pun")
  print(r.content)
