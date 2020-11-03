import pytest
import requests
import json

#Get the first bucket data from Tokens file
tFile = open(r"TestData\\Tokens.txt")
tFileSplit = tFile.read().split(":")
basket = tFileSplit[0]
token = tFileSplit[1]
tFile.close()

def test_basket_get():
    url = "https://rbaskets.in/api/baskets/"+basket + "InvalidNameBasketTest"
    headers = {
        "Authorization": token
    }
    response = requests.get(url, headers=headers)

    assert response.status_code == 404

    #What are the invalid basket names???
