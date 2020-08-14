import requests

r = requests.get("https://newsapi.org/docs/get-started")
print(r.text)
