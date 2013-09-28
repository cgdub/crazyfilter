import requests

userid = "45183546"

res = requests.get(
    "http://api.nytimes.com/svc/community/v2/comments/user/id/"
    + userid + ".json?&api-key=5c80aa20d61dec8a332aea8ad7c7c0d7:3:68189777")

data = res.json()

print data

