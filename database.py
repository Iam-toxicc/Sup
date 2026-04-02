from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["store"]

users = db["users"]

def add_user(user_id, name):
    users.update_one(
        {"user_id": user_id},
        {"$setOnInsert": {"name": name, "balance": 0}},
        upsert=True
    )

def update_balance(user_id, amount):
    users.update_one({"user_id": user_id}, {"$inc": {"balance": amount}})

def get_user(user_id):
    return users.find_one({"user_id": user_id})
