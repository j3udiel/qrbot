from flask import Flask, jsonify
from threading import Thread
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import qrcode
from io import BytesIO
import os

# Configuración del servidor web para el health check
app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify(status="ok")

# Función para iniciar el servidor Flask en un hilo separado
def run_flask():
    app.run(port=5000)

# Función para manejar mensajes que contienen texto
def handle_message(update, context):
    text = update.message.text
    qr = qrcode.make(text)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    update.message.reply_photo(photo=buffer)

# Función principal para el bot de Telegram
def main():
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    if not telegram_token:
        raise RuntimeError('No se encontró la variable de entorno TELEGRAM_TOKEN')

    updater = Updater(token=telegram_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Iniciar el bot en un hilo separado
    Thread(target=updater.start_polling).start()

    # Iniciar el servidor Flask para el health check
    run_flask()

if __name__ == '__main__':
    main()
