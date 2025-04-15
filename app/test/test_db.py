#from app.db import get_questions
#from app.trivia import Question
#from app.quiz import Quiz

#def test_get_questions_from_db():
#    questions = get_questions()
#    assert isinstance(questions, list)
#   assert len(questions) > 0  # Verifica que haya preguntas en la DB

#    desc, options, correct, diff = questions[0]
#    assert isinstance(desc, str)
#    assert isinstance(options, list)
#    assert isinstance(correct, int)
#    assert diff in ['Fácil', 'Media', 'Difícil']
# Verifica que Quiz pueda cargar todas las preguntas de la DB y que funcionen correctamente
#def test_quiz_with_real_questions():
#    quiz = Quiz()
#    questions = get_questions()

#    for desc, options, correct, diff in questions:
#        q = Question(desc, options, correct, diff)
#        quiz.add_question(q)

#    assert len(quiz.questions) == len(questions)

#    question = quiz.get_next_question()
#    assert isinstance(question, Question)
#    assert isinstance(question.description, str)
#    assert len(question.options) >= 2