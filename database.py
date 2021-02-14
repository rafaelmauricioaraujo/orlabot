from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("DATABASE"))
db = client.orla

def find_project():
    print('find project called')
    return db.project.find({})

def close():
    return client.close()