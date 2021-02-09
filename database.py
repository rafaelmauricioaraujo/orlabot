from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("DATABASE"))
db = client.orla

def find_project():
    return db.project.find({})

def close():
    return client.close()