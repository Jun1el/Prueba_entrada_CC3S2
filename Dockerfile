# Imagen de Python
FROM python:3.10-slim
# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Instalamos dependencias usando requirements

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos los archivos al contenedor
COPY . .

# Puerto donde correrá la app
EXPOSE 8000

# Comando para ejecutar la app(Por defecto, en documentacion)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

