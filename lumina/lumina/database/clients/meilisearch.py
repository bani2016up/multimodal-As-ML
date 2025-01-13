
import meilisearch


class MeilisearchClient:
    def __init__(self, meilisearch_url: str, meilisearch_key: str):
        self.meilisearch_client = meilisearch.Client(meilisearch_url, meilisearch_key)
        self.index = self.meilisearch_client.index('documents')
