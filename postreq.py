#!/usr/bin/python3

"""
    login.py

    MediaWiki API Demos
    Demo of `Login` module: Sending post request to login
    MIT license
"""

import requests
import sqlalchemy as db
import pandas as pd

lgname=input("Enter username: ")
lgpassword=input("Enter password: ")
S = requests.Session()

URL = "https://www.mediawiki.org/w/api.php"

# Retrieve login token first
PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

print(LOGIN_TOKEN)

# Send a post request to login. Using the main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_1 = {
    'action':"login",
    'lgname':lgname,
    'lgpassword':lgpassword,
    'lgtoken':LOGIN_TOKEN,
    'format':"json"
}

R = S.post(URL, data=PARAMS_1)
DATA = R.json()

print(DATA)

data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
pd.DataFrame.from_dict(data)