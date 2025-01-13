import os

from bson import ObjectId
from datetime import datetime

from .utils import id_convert
from .clients.mongodb import MongoClient
from .clients.meilisearch import MeilisearchClient
from .schemas import Message, MessageResult, MessagesQueryResult


class DocumentStore:
    def __init__(
        self, mongo_uri: str = "", meilisearch_url: str = "", meilisearch_key: str = ""
    ):
        self.mongo = MongoClient(os.environ.get("MONGO_URI", mongo_uri))
        self.meilisearch = MeilisearchClient(
            os.environ.get("MEILISEARCH_URL", meilisearch_url),
            os.environ.get("MEILISEARCH_KEY", meilisearch_key),
        )

    def add(self, document: Message) -> str:
        result = self.mongo.collection.insert_one(document.model_dump())
        document_id = str(result.inserted_id)
        self.meilisearch.index.add_documents(
            [{**document.model_dump(), "id": document_id}]
        )
        return document_id

    def get_by_id(self, document_id: str) -> MessageResult:
        document = self.mongo.collection.find_one({"_id": ObjectId(document_id)})
        id_convert(document)
        return MessageResult.model_validate(document)

    def get_by_time_range(
        self, start_time: datetime, end_time: datetime
    ) -> MessagesQueryResult:
        documents = list(
            self.mongo.collection.find(
                {"timestamp": {"$gte": start_time, "$lte": end_time}}
            )
        )
        id_convert(documents)
        return MessagesQueryResult(results=[MessageResult.model_validate(doc) for doc in documents])

    def get_by_word(self, match: str) -> MessagesQueryResult:
        search_results = self.meilisearch.index.search(match)
        document_ids = [result["id"] for result in search_results["hits"]]
        documents = list(
            self.mongo.collection.find(
                {"_id": {"$in": [ObjectId(id) for id in document_ids]}}
            )
        )
        id_convert(documents)
        return MessagesQueryResult(results=[MessageResult.model_validate(doc) for doc in documents])

    def all(self) -> MessagesQueryResult:
        documents = list(self.mongo.collection.find())
        id_convert(documents)
        return MessagesQueryResult(results=[MessageResult.model_validate(doc) for doc in documents])
