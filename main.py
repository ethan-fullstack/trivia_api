from fastapi import FastAPI
from typing import List
import random
from models import Question, QuestionCreate, AnswerRequest, AnswerResult

app = FastAPI(title="Trivia Rápida+", version="1.1")

# Datos simulados (base temporal en memoria)
questions: List[Question] = [
    Question(
        id=1,
        title="¿Cuál es el planeta más grande?",
        options=["Marte", "Júpiter", "Tierra", "Neptuno"],
        answer_index=1,
        category="science",
    ),
    Question(
        id=2,
        title="¿Quién pintó la Mona Lisa?",
        options=["Van Gogh", "Da Vinci", "Picasso", "Dalí"],
        answer_index=1,
        category="art",
    ),
]


@app.get("/")
def home():
    return {"message": "Trivia API running!"}


@app.get("/questions", response_model=List[Question])
def get_questions():
    return questions


@app.get("/questions/{question_id}", response_model=Question)
def get_question(question_id: int):
    for q in questions:
        if q.id == question_id:
            return q
    return {"error": "Question not found"}


@app.post("/questions", response_model=Question)
def create_question(question: QuestionCreate):
    new_id = len(questions) + 1
    q = Question(id=new_id, **question.dict())
    questions.append(q)
    return q


@app.post("/answer", response_model=AnswerResult)
def check_answer(answer: AnswerRequest):
    for q in questions:
        if q.id == answer.question_id:
            correct = q.answer_index == answer.selected_index
            return AnswerResult(correct=correct, correct_index=q.answer_index)
    return {"error": "Question not found"}


@app.get("/random", response_model=Question)
def random_question():
    return random.choice(questions)
