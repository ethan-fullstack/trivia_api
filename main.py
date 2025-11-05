from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import random

# Instancia principal de la app
app = FastAPI(title="Trivia Rápida+", version="1.0")

# ----- Modelos de datos (Pydantic) -----
class Question(BaseModel):
    id: int
    title: str
    options: List[str]
    answer_index: int
    category: str

class QuestionCreate(BaseModel):
    title: str
    options: List[str]
    answer_index: int
    category: str

# ----- Datos simulados -----
questions = [
    {"id": 1, "title": "¿Cuál es el planeta más grande del sistema solar?",
     "options": ["Marte", "Júpiter", "Saturno", "Tierra"], "answer_index": 1, "category": "science"},
    {"id": 2, "title": "¿Quién pintó la Mona Lisa?",
     "options": ["Picasso", "Da Vinci", "Van Gogh", "Dalí"], "answer_index": 1, "category": "art"},
]

# ----- Rutas principales -----
@app.get("/")
def read_root():
    """Ruta base: mensaje de bienvenida"""
    return {"message": "Welcome to Trivia Rápida+ API!"}

@app.get("/questions")
def get_all_questions():
    """Devuelve todas las preguntas"""
    return questions

@app.get("/questions/{question_id}")
def get_question_by_id(question_id: int):
    """Devuelve una pregunta según su ID"""
    for q in questions:
        if q["id"] == question_id:
            return q
    return {"error": "Question not found"}

@app.post("/questions")
def create_question(question: QuestionCreate):
    """Agrega una nueva pregunta"""
    new_id = len(questions) + 1
    new_question = question.dict()
    new_question["id"] = new_id
    questions.append(new_question)
    return {"message": "Question created successfully!", "data": new_question}

@app.get("/random")
def get_random_question():
    """Devuelve una pregunta aleatoria"""
    return random.choice(questions)
