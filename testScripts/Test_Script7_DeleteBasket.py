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
    url = "https://rbaskets.in/api/baskets/"+basket
    headers = {
        "Authorization": token
    }
    response = requests.delete(url, headers=headers)
    print(response.text)
    assert response.status_code == 204

    #Get the basket to check
