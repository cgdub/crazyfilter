from pymongo import MongoClient
import json

client = MongoClient()
db = client.comments

comments = db.nutcases.find({}, { "results.comments.commentBody": 1})

for entry in comments:
    if entry.has_key("results"):
        if entry.get("results").has_key("comments"):
            for comment in entry.get("results").get("comments"):
                print comment.get("commentBody")
