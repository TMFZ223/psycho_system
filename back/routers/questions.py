from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from schemas.question_create_schema import QuestionCreateSchema
from database import SessionLocal
from db_table_models.question import Question
from db_table_models.answer import Answer
from deps import get_current_user, get_admin_user

router = APIRouter(prefix="/questions", tags=["Questions"])


async def get_db():
    async with SessionLocal() as db:
        yield db


@router.get("")
async def get_questions(
    user=Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Question).options(selectinload(Question.answers))
    )
    questions = result.scalars().all()

    data = []
    for q in questions:
        data.append({
            "id": q.id,
            "text": q.question_text,
            "answers": [
                {
                    "id": a.id,
                    "variant": a.variant,
                    "position": a.position
                }
                for a in sorted(q.answers, key=lambda x: x.position or 0)
            ]
        })

    return {
        "success": True, "status": 200,
        "data": data
    }

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_question(
    data: QuestionCreateSchema,
    user=Depends(get_admin_user),
    db: AsyncSession = Depends(get_db)
):
    # создаём вопрос
    question = Question(question_text=data.question_text)

    db.add(question)
    await db.flush()  # получаем question.id

    # создаём ответы
    for ans in data.answers:
        answer = Answer(
            question_id=question.id,
            variant=ans.variant,
            score=ans.score,
            position=ans.position
        )
        db.add(answer)

    await db.commit()

    return {
        "success": True, "status": 200, "data": {"message": "question inserted"}
    }

@router.delete("/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_question(
    question_id: int,
    user=Depends(get_admin_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Question).where(Question.id == question_id)
    )
    question = result.scalar_one_or_none()

    if not question:
        raise HTTPException(
            status_code=404,
            detail="question not found"
        )

    await db.delete(question)
    await db.commit()
