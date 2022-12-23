import requests

url = "http://127.0.0.1:8000/api/v1/todos/"

data = {
    "name": "Bugun DRF ni organaman.",
    "completed": False
}

res = requests.post(url, data)

print(res.text)