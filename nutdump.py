import requests
from pymongo import MongoClient
from sys import argv

script, filename = argv

with open(filename) as f:
    userlist = f.readlines()

for userid in userlist:
    userid = userid.strip()
    if userid.isdigit():
        print userid
        client = MongoClient()
        db = client.comments
        collection = db.nutcases
        res = requests.get(
                "http://api.nytimes.com/svc/community/v2/comments/user/id/"
                + userid +
                ".json?&api-key=5c80aa20d61dec8a332aea8ad7c7c0d7:3:68189777")
        data = res.json()
        collection.insert(data)

