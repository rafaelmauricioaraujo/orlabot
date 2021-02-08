from pymongo import MongoClient

client = MongoClient("mongodb+srv://rasa:Y3XMzsBIO5i1N9Re@cluster0.tpni9.mongodb.net/orla?retryWrites=true&w=majority")
db = client.orla

def find():
    return db.project.find({})

def close():
    return client.close()