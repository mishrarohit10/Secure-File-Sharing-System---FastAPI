from pymongo import mongo_client
import pymongo
from app.config import settings

client = mongo_client.MongoClient(settings.DATABASE_URL)
print('Connected to MongoDB...')

db = client[settings.MONGO_DATABASE]
User = db.users
File = db.files
User.create_index([("email", pymongo.ASCENDING)], unique=True)
File.create_index([("url_token", pymongo.ASCENDING)], unique=True)
