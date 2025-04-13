import psycopg2

def get_connection():
    # conexion a la base de datos  
    return psycopg2.connect(
        dbname="trivia_db",
        user="postgres",
        password="postgres",
        host="db",
        port="5432"
    )

def get_questions():
    conn = get_connection()# Establecemos la conexión a la base de datos
    cur = conn.cursor()# Creamos un cursor para ejecutar la consulta SQL
    # Ejecutamos la consulta para obtener las primeras 10 preguntas
    cur.execute("SELECT description, options, correct_answer, difficulty FROM questions LIMIT 10")
    rows = cur.fetchall()# Obtienemos todas las filas resultantes de la consulta
    cur.close() # Cierra el cursor
    conn.close() # Cerramos la conexión a la base de datos
    
    questions = []# Lista para almacenar las preguntas procesadas
    for desc, options, correct, diff in rows:
        # Convertimos opciones de string a lista si viene en formato string
        if isinstance(options, str):
            options = options.strip('{}').split(',')
        questions.append((desc, options, correct, diff))
    return questions
