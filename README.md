# Bot de Telegram que devuelve un QR en DigitalOcean

Este repositorio contiene el código para un bot de Telegram diseñado para ser desplegado en DigitalOcean App Platform como un worker. El bot responde a los mensajes de los usuarios y realiza tareas específicas definidas en el código.

## Estructura del Proyecto

El proyecto consta de los siguientes archivos principales:

- `bot.py`: Script principal del bot de Telegram.
- `requirements.txt`: Archivo que lista todas las dependencias necesarias para ejecutar el bot.
- `Procfile`: Archivo de configuración para DigitalOcean que especifica cómo ejecutar el bot.

## `bot.py`

Este script es el núcleo del bot. Utiliza la biblioteca `python-telegram-bot` para interactuar con la API de Telegram. El bot está configurado para escuchar y responder a mensajes específicos de los usuarios.

## `requirements.txt`

Este archivo contiene todas las dependencias necesarias para que el bot funcione correctamente. Incluye:

