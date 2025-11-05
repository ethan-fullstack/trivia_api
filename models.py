# models.py
from pydantic import BaseModel, Field
from typing import List


# Modelo para crear una nueva pregunta
class QuestionCreate(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    options: List[str] = Field(..., min_items=4, max_items=4)  # type: ignore
    answer_index: int = Field(..., ge=0, le=3)
    category: str


# Modelo para mostrar una pregunta completa
class Question(QuestionCreate):
    id: int


# Modelo para evaluar una respuesta
class AnswerRequest(BaseModel):
    question_id: int
    selected_index: int


# Resultado de la evaluación
class AnswerResult(BaseModel):
    correct: bool
    correct_index: int
