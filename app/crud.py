from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Note


async def get_all_notes(db: AsyncSession):
    result = await db.execute(select(Note))
    return result.scalars().all()


async def get_note_by_id(db: AsyncSession, note_id: int):
    result = await db.execute(select(Note).where(Note.id == note_id))
    return result.scalars().first()


async def create_note(db: AsyncSession, title: str, content: str):
    new_note = Note(title=title, content=content)
    db.add(new_note)
    await db.commit()
    await db.refresh(new_note)
    return new_note


async def update_note(
    db: AsyncSession,
    note_id: int,
    title: str = None,
    content: str = None,
    done: bool = None,
):
    note = await get_note_by_id(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    if title is not None:
        note.title = title
    if content is not None:
        note.content = content
    if done is not None:
        note.done = done

    await db.commit()
    await db.refresh(note)
    return note


async def delete_note(db: AsyncSession, note_id: int):
    note = await get_note_by_id(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    await db.delete(note)
    await db.commit()
    return {"ok": True}
