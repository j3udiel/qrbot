import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import qrcode
from io import BytesIO
import os

# Configuración del logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Función para manejar mensajes que contienen texto
def handle_message(update, context):
    text = update.message.text
    # Generar un código QR a partir del texto
    qr = qrcode.make(text)
    
    # Guardar la imagen en un buffer para enviarla
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    
    # Enviar la imagen como respuesta
    update.message.reply_photo(photo=buffer)

# Función de error
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Función principal
def main():
    # Obtener el token del bot desde la variable de entorno
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    if not telegram_token:
        raise RuntimeError('No se encontró la variable de entorno TELEGRAM_TOKEN')

    # Crear el Updater y pasarle el token del bot
    updater = Updater(token=telegram_token, use_context=True)

    # Obtener el dispatcher para registrar handlers
    dp = updater.dispatcher

    # Registrar el handler para los mensajes
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Registrar el handler de errores
    dp.add_error_handler(error)

    # Iniciar el bot
    updater.start_polling()

    # Ejecutar el bot hasta que se presione Ctrl-C o el proceso reciba SIGINT,
    # SIGTERM o SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
