from trivia import Question
from quiz import Quiz
from db import get_questions
def run_quiz():
    quiz = Quiz()
    try:
        for desc, options, correct, diff in get_questions():
            q = Question(desc, options, correct, diff)
            quiz.add_question(q)
    except Exception as e:
        print(f"Error al cargar preguntas desde la base de datos: {e}")
        return

    while True:
        question = quiz.get_next_question()
        if not question:
            print("¡Juego terminado!")
            break

        print(f"\n{question.description} (Dificultad: {question.difficulty})")
        for idx, option in enumerate(question.options):
            print(f"{idx}. {option}")
        
        try:
            answer = int(input("Elige tu respuesta (número): "))
            if quiz.answer_question(question, answer):  # Aquí usamos el método answer_question
                print("¡Correcto!")
            else:
                print(f"Incorrecto. La respuesta correcta era: {question.options[question.correct_answer]}")
        except Exception as e:
            print(f"Error: {e}")
    print("\n--- Resultado final ---")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")

if __name__ == "__main__":
    run_quiz()
