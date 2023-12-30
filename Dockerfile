# Utilizar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor y instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente al contenedor
COPY . .

# Definir la variable de entorno para el token de Telegram (deberás proporcionarla al ejecutar el contenedor)
ENV TELEGRAM_TOKEN="TuTokenDeTelegramAquí"

# Comando para ejecutar el bot
CMD ["python", "./bot.py"]

