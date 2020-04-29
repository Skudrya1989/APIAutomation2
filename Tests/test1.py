import requests
import json
import jsonpath
import pytest


def test_some_test():
    url = "https://reqres.in"
    params = {'page': 2}
    # url = "Base_URL + "/api/users" , params=params"
# print(json.dumps(response.json(), indent=4))
# print(response.content)
    response = requests.get(url + "/api/users", params=params)
    json_response = json.loads(response.text)
    pages = jsonpath.jsonpath(json_response, 'total_pages')
    print(response.text)
    assert pages[0] == 2
    assert response.status_code == 200
    assert response.status_code == 200
    assert response.status_code == 202
    assert response.status_code == 201
    assert response.status_code == 201
    assert response.status_code == 201