from fastapi import APIRouter, HTTPException
from .models import Note, notes_db

router = APIRouter()


@router.post("/notes", response_model=Note)
async def create_note(note: Note):
    notes_db.append(note)
    return note


@router.get("/notes", response_model=list[Note])
async def get_notes():
    return notes_db
