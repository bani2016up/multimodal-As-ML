from pydantic import BaseModel
from database import DocumentStore

class Node(BaseModel):
    db_id: str
    _call_counter: int

type Task = str
type SortedByCallList = list[Node]

class Connectome:

    def __init__(self, ds: DocumentStore):
        self.ds: DocumentStore = ds
        self._map: dict[Task, SortedByCallList] = {}

    def get(self, topic: str):
