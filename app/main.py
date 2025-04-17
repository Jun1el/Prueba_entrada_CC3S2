from trivia import Question
from quiz import Quiz
from db import get_questions

# mostramos titulo del juego
def mostrar_titulo():
    print("""
========================================
    🎉 BIENVENIDO A LA TRIVIA 🎉
========================================
Responde las preguntas escribiendo el número 
de la opción correcta. ¡Buena suerte!
""")

""" 
    Inicia el juego, cargamos las preguntas desde la base de datos,muestra las preguntas y nos permite responder.
    El juego termina cuando se responden todas las preguntas o si ocurre un error al cargar las preguntas.

    En cada pregunta:
        - Muestra la pregunta y las opciones.
        - Permite al usuario seleccionar una respuesta.
        - Verifica si la respuesta es correcta y muestra el puntaje correspondiente.
        
    Al finalizar:
        - Muestra un resumen del puntaje y las respuestas correctas/incorrectas.
"""

def run_quiz():
    print("¡Bienvenido al juego de Trivia!")
    print("Instrucciones:")
    print("Responde las preguntas escribiendo el número de la opción correcta.\n")
    quiz = Quiz() # Creamos una instancia de Quiz
    try:
        # cargamos las preguntas desde la base de datos
        for desc, options, correct, diff in get_questions():
            # Creamos una nueva instancia de la pregunta y la agregamos al qui
            q = Question(desc, options, correct, diff)
            quiz.add_question(q)
    except Exception as e:
        print(f"Error al cargar preguntas desde la base de datos: {e}")
        return

    while True:
        # Obtiene la siguiente pregunta
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
            # El jugador selecciona su respuesta
            answer = int(input("\n Tu respuesta (número): "))
            # Verificamos si la respuesta es correcta y actualizamos el puntaje
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
