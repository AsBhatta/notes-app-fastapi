from pydantic import BaseModel
from typing import List


class Note(BaseModel):
    title: str
    content: str


# Temporary in-memory database
notes_db: List[Note] = []
