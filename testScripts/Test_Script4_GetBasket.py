import pytest
import requests
import json

#Get the first bucket data from Tokens file
tFile = open(r"TestData\\Tokens.txt")
tFileSplit = tFile.read().split(":")
basket = tFileSplit[0]
token = tFileSplit[1]
tFile.close()

#Get body data for basket creation settings
basketBodyData = open(r"TestData\CreateBasketBody.json", 'r')
json_input = basketBodyData.read()
request_json = json.loads(json_input)

def test_basket_get():
    url = "https://rbaskets.in/api/baskets/" + basket

    headers = {
        'Authorization': token
    }

    response = requests.put(url, json=request_json, headers=headers)

    writeText = str(response.content)
    tFile = open(r"TestData\responses.txt", "a")
    tFile.writelines('\n' + basket + writeText)
    tFile.close()
    assert (response.status_code == 204)