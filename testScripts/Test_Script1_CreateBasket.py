import pytest
import requests
import json

#print(sendBodyDict)

#for key in sendBodyDict:


basket = "KoshnicaTest56"
def test_basket_create():

    # Get body data for basket creation settings
    basketBodyData = open("TestData\\CreateBasketBody.json", 'r')
    json_input = basketBodyData.read()
    reqest_json = json.loads(json_input)

    url = "https://rbaskets.in/api/baskets/"+basket
    headers ={
        "Content-Type": "application/json;charset=UTF-8"
    }

    response = requests.post(url, json=reqest_json, headers=headers)
    writeText = str(response.content)
    tFile = open(r"TestData\\Tokens.txt", "w")
    tFileHistory = open(r"TestData\\OldTokens.txt", "a")
    tFileHistory.writelines(basket + ":" + writeText[12:56] + '\n')
    tFile.writelines(basket + ":" + writeText[12:56]) #Save the created basket token to file
    tFileHistory.close()
    tFile.close()
    #assert (response.status_code == 201)

    # compare data send and basket body
    headers = {
        "Authorization": writeText[12:56]
    }

    response = requests.get(url, headers=headers)
   # respLen = len(response.content)
    respBody = str(response.content)

    json_input = replace_string(json_input)
    sendBodyDict = dict(map(str.strip, s.split(':', 1)) for s in json_input.split(',') if ':' in s) #formating dictionary

    respBody = respBody.strip('b')
    respBody = replace_string(respBody)
    receivedBodyDict = dict(map(str.strip, s.split(':', 1)) for s in respBody.split(',') if ':' in s) #formating dictionary

    compare_dict(sendBodyDict, receivedBodyDict)
   # -print(sendBodyDict)


def replace_string(forStrip):
    forStrip = forStrip.replace('{', '').replace('}', '').replace('"', '').replace("'", '')
    return forStrip

def compare_dict(dict1, dict2):
    for key in dict1:
        assert  key in dict2
