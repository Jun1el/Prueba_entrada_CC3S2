import psycopg2
from dotenv import load_dotenv
import os

load_dotenv('.env')
def get_connection():
    # conexion a la base de datos  
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
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
