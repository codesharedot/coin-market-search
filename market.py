#!/usr/bin/python3
import requests
import json
import os

coin = input("Coin: ")

api_url = "https://coinmarketbook.cc/api/ticker/" + coin
response = requests.get(api_url)
response_json = response.json()
#print(response_json)
#print(response_json['markets'])

for market in response_json['markets']:
    if "EUR" in market:
        print(market)
