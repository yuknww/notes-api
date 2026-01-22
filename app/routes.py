from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import (
    get_all_notes,
    create_note,
    update_note,
    get_note_by_id,
    delete_note,
)
from app.database import get_db
from app.schemas import NoteBase, NoteCreate, NoteUpdate, NoteResponse

router = APIRouter()


@router.get("/notes", response_model=List[NoteBase])
async def read_notes(db: AsyncSession = Depends(get_db)):
    """Возвращает все существующие заметки"""
    notes_list = await get_all_notes(db)
    if not notes_list:
        raise HTTPException(status_code=404, detail="No notes found")

    return notes_list


@router.get("/notes/{note_id}", response_model=NoteBase)
async def read_note_by_id(note_id: int, db: AsyncSession = Depends(get_db)):
    """Возвращает заметку по id"""
    note = await get_note_by_id(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.post("/notes", response_model=NoteResponse)
async def create_note_route(note: NoteCreate, db: AsyncSession = Depends(get_db)):
    """Создаёт заметку"""
    note = NoteCreate(**note.model_dump())
    new_note = await create_note(db=db, title=note.title, content=note.content)
    return new_note


@router.put("/notes/{note_id}", response_model=NoteResponse)
async def update_note_route(
    note_id: int, note: NoteUpdate, db: AsyncSession = Depends(get_db)
):
    """Обновляет любой параметр заметки по id"""
    note = NoteUpdate(**note.model_dump())
    upd_note = await update_note(
        db=db, note_id=note_id, title=note.title, content=note.content, done=note.done
    )
    return upd_note


@router.delete("/notes/{note_id}")
async def delete_note_route(note_id: int, db: AsyncSession = Depends(get_db)):
    """Удаляет заметку по id"""
    deleted_note = await delete_note(db, note_id)
    return deleted_note
