import json
import requests

URL = "http://127.0.0.1:8000/parsedata"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


get_data()


def post_data():
    data = {
        "name": "mile",
        "stu_id": 23,
        "place": "LA"
    }
    try:
        json_data = json.dumps(data)
        r = requests.post(url=URL, data=json_data)
        data = r.json()
        print(data)
    except Exception as e:
        print(e)


# post_data()
