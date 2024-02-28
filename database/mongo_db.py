from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from config import settings

client: MongoClient = MongoClient(host=settings.MONGO_URL)
db: Database = client[settings.MONGO_CLIENT]
collection: Collection = db[settings.MONGO_COLLECTION]
