import pytest
from app.trivia import Question

def test_question_correct_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], 3, "fácil")
    assert question.is_correct(3)

def test_question_incorrect_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], 3, "fácil")
    assert not question.is_correct(2)

def test_correct_answer():
    q = Question("¿Capital de Perú?", ["Lima", "Cusco", "Arequipa"], 0, "fácil")
    assert q.is_correct(0)

def test_incorrect_answer():
    q = Question("¿Capital de Perú?", ["Lima", "Cusco", "Arequipa"], 0, "fácil")
    assert not q.is_correct(2)

def test_invalid_correct_answer_index():
    with pytest.raises(ValueError):
        Question("¿Pregunta inválida?", ["A", "B"], 5, "media")
    
def test_not_enough_options():
    with pytest.raises(ValueError):
        Question("¿Pregunta inválida?", ["Solo una opción"], 0, "difícil")