# Imagen de Python
FROM python:3.10-slim
# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos al contenedor
COPY . .

# Instalamos dependencias
RUN pip install --no-cache-dir fastapi uvicorn asyncpg databases

# Puerto donde correrá la app
EXPOSE 8000

# Comando para ejecutar la app(Por defecto, en documentacion)
CMD ["uvicorn", "app.main:app:app", "--host", "0.0.0.0", "--port", "8000"]

