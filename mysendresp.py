import requests
import json

URL = "http://127.0.0.1:8000/D/"

data = {
    'name': 'sujal',
    'stu_id': 11,
    'place': 'up',
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

data = r.json()
print(data)
