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

def test_answer_correct():
    quiz = Quiz()
    question = Question("¿2+2?", ["3", "4"], 1, "fácil")
    quiz.add_question(question)
    
    q = quiz.get_next_question()
    result = quiz.answer_question(q, 1)

    assert result is True
    assert quiz.correct_answers == 1
    assert quiz.incorrect_answers == 0

def test_answer_incorrect():
    quiz = Quiz()
    question = Question("¿2+2?", ["3", "4"], 1, "fácil")
    quiz.add_question(question)
    
    q = quiz.get_next_question()
    result = quiz.answer_question(q, 0)

    assert result is False
    assert quiz.correct_answers == 0
    assert quiz.incorrect_answers == 1
