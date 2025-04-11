class Question:
    def __init__(self, description, options, correct_answer, difficulty):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty
## Verificamos que la respuesta correcta sera un entero y que este dentro del rango de opciones 
        if not isinstance(correct_answer, int) or not 0 <= correct_answer < len(options):
            raise ValueError("El índice de la respuesta correcta es inválido.")
## Evitar crear preguntas con menos de 2 opciones
        if len(options) < 2:
            raise ValueError("Debe haber al menos dos opciones.")

    def is_correct(self, answer):
        if not isinstance(answer, int):
            ## lanzamos una excepcion si la respuesta no es un entero
            raise TypeError("answer_index debe ser un entero.")
        return self.correct_answer == answer
    
class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    
def run_quiz():
    quiz = Quiz()
    # Creamos preguntas usando índices para respuestas correctas
    q1 = Question("¿Cuál es la capital de Perú?", ["Lima", "Cusco", "Arequipa"], 0, "Fácil")
    q2 = Question("¿Cuánto es 2 + 2?", ["3", "4", "5"], 1, "Fácil")
    
    quiz.add_question(q1)
    quiz.add_question(q2)

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
            if question.is_correct(answer):
                print("¡Correcto!")
            else:
                print(f"Incorrecto. La respuesta correcta era: {question.options[question.correct_answer]}")
        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    run_quiz()