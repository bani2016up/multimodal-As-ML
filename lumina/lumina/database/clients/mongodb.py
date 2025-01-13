from pymongo import MongoClient as _MongoClient


class MongoClient:
    def __init__(self, mongo_uri: str):
        self.mongo_client = _MongoClient(mongo_uri)
        self.db = self.mongo_client.document_store
        self.collection = self.db.documents
