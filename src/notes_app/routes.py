from fastapi import APIRouter
from notes_app.models import Note, notes_db

router = APIRouter()

@router.post("/notes", response_model=Note, status_code=201, tags=["Notes"])
async def create_note(note: Note):
    notes_db.append(note)
    return note

@router.get("/notes", response_model=list[Note], tags=["Notes"])
async def get_notes():
    return notes_db
