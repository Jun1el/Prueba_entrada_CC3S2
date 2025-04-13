import pytest
from app.quiz import Quiz
from app.trivia import Question

def test_add_and_get_question():
    quiz = Quiz()
    question = Question("¿Capital de Perú?", ["Lima", "Cusco"], 0, "fácil")
    quiz.add_question(question)
    
    retrieved = quiz.get_next_question()
    assert retrieved.description == "¿Capital de Perú?"
    assert quiz.get_next_question() is None
## test que la pregunta se añade correctamente y se obtiene en dificultad fácil
def test_answer_correct_easy():
    quiz = Quiz()
    question = Question("¿2+2?", ["3", "4"], 1, "Fácil")
    quiz.add_question(question)

    q = quiz.get_next_question()
    result = quiz.answer_question(q, 1)

    assert result is True
    assert quiz.correct_answers == 1
    assert quiz.incorrect_answers == 0
    assert quiz.score == 1  
## test que la pregunta se responde correctamente y se obtiene en dificultad media 
def test_answer_correct_medium():
    quiz = Quiz()
    question = Question("¿Capital de España?", ["Madrid", "Barcelona"], 0, "Media")
    quiz.add_question(question)

    q = quiz.get_next_question()
    result = quiz.answer_question(q, 0)

    assert result is True
    assert quiz.correct_answers == 1
    assert quiz.score == 2 

## test que la pregunta se responde correctamente y se obtiene en dificultad difícil
def test_answer_correct_hard():
    quiz = Quiz()
    question = Question("¿Año de la caída de Constantinopla?", ["1453", "1492"], 0, "Difícil")
    quiz.add_question(question)

    q = quiz.get_next_question()
    result = quiz.answer_question(q, 0)

    assert result is True
    assert quiz.correct_answers == 1
    assert quiz.score == 3  # Difícil = 3 puntos

# test para respuesta incorrecta 
def test_answer_incorrect():
    quiz = Quiz()
    question = Question("¿2+2?", ["3", "4"], 1, "Fácil")
    quiz.add_question(question)

    q = quiz.get_next_question()
    result = quiz.answer_question(q, 0)

    assert result is False
    assert quiz.correct_answers == 0
    assert quiz.incorrect_answers == 1
    assert quiz.score == 0

def test_get_points_for_question():
    quiz = Quiz()
    q_easy = Question("...", ["a", "b"], 0, "Fácil")
    q_med = Question("...", ["a", "b"], 0, "Media")
    q_hard = Question("...", ["a", "b"], 0, "Difícil")

    assert quiz.get_points_for_question(q_easy) == 1
    assert quiz.get_points_for_question(q_med) == 2
    assert quiz.get_points_for_question(q_hard) == 3
