from trivia import Question
from quiz import Quiz
from db import get_questions

def mostrar_titulo():
    print("""
========================================
    🎉 BIENVENIDO A LA TRIVIA 🎉
========================================
Responde las preguntas escribiendo el número 
de la opción correcta. ¡Buena suerte!
""")

def run_quiz():
    print("¡Bienvenido al juego de Trivia!")
    print("Instrucciones:")
    print("Responde las preguntas escribiendo el número de la opción correcta.\n")
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
        
        print("----------------------------------------")
        print(f"📌 Pregunta: {question.description}")
        print(f"🎯 Dificultad: {question.difficulty}")
        print("----------------------------------------")
        for idx, option in enumerate(question.options):
            print(f"{idx}. {option}")
        
        try:
            answer = int(input("\n Tu respuesta (número): "))
            correcta = quiz.answer_question(question, answer)
            puntos = quiz.get_points_for_question(question)
            if correcta:
                print(f"\n ¡Correcto! +{puntos} punto(s)\n")
            else:
                correcta_texto = question.options[question.correct_answer]
                print(f"\n Incorrecto. La respuesta correcta era: {correcta_texto}")
                print(f"0 puntos\n")
        except Exception as e:
            print(f"\n[ERROR] Entrada inválida: {e}\n")
            
    print("\n--- Resultado final ---")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")
    print(f"Puntaje total: {quiz.score}")

if __name__ == "__main__":
    run_quiz()
