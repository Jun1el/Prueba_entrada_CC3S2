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
    