import requests

data = requests.get("https://randomuser.me/api/?result=1").json()
print(type(data['results']))