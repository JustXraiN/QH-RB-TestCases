import pytest
import requests
import json

#Get the first bucket data from Tokens file
tFile = open(r"TestData\\Tokens.txt")
tFileSplit = tFile.read().split(":")
basket = tFileSplit[0]
tFile.close()

def test_basket_get():
    url = "https://rbaskets.in/api/baskets/"+basket
    headers = {
        "Authorization": ""
    }
    response = requests.get(url, headers=headers)

    assert response.status_code == 401