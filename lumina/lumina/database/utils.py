

from typing import Any


type Has_idKey = dict[str | Any, Any]

def _id_convert(doc: Has_idKey) -> None:
    doc['_id'] = str(doc['_id'])

def id_convert(docs: Has_idKey | list[Has_idKey]) -> None:
    if docs == [] or docs is None:
        return
    if not isinstance(docs, list):
        docs = [docs]
    [_id_convert(doc) for doc in docs]
