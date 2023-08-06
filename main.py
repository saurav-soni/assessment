import json
import requests


def post_request():
    url = 'https://demo.onefin.in/api/v1/usermodule/login/'
    body = {
        "username": "testuser",
        "password": "v^4!C%CQ94f0"
    }

    resp = requests.post(url, data=json.dumps(body), headers={"Content-Type": "application/json"})

    response = resp.json()
    token = response["data"]["token"]
    return token


def get_request(token):
    get_url = "https://demo.onefin.in/api/v1/maya/movies/"
    response = requests.get(get_url, headers={"authorization": token})
    return response.json()


if __name__ == '__main__':
    token = post_request()
    print(get_request(token))
