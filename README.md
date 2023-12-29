# Bot de Telegram que devuelve un QR en DigitalOcean

Este repositorio contiene el código para un bot de Telegram diseñado para ser desplegado en DigitalOcean App Platform como un worker. El bot responde a los mensajes de los usuarios y realiza tareas específicas definidas en el código.

Lo puedes probar aqui 

## Estructura del Proyecto

El proyecto consta de los siguientes archivos principales:

- `bot.py`: Script principal del bot de Telegram.
- `requirements.txt`: Archivo que lista todas las dependencias necesarias para ejecutar el bot.
- `Procfile`: Archivo de configuración para DigitalOcean que especifica cómo ejecutar el bot.

## `bot.py`

Este script es el núcleo del bot. Utiliza la biblioteca `python-telegram-bot` para interactuar con la API de Telegram. El bot está configurado para escuchar y responder a mensajes específicos de los usuarios.

## `requirements.txt`

Este archivo contiene todas las dependencias necesarias para que el bot funcione correctamente. Incluye:


Esto indica que la aplicación debe ejecutar `bot.py` en un worker.

## Despliegue en DigitalOcean

Para desplegar este bot en DigitalOcean App Platform como un worker, sigue estos pasos:

1. **Crea una Aplicación en DigitalOcean App Platform.**
   - Elige el método de fuente de tu código (por ejemplo, GitHub).
   - Conecta tu repositorio y selecciona la rama correspondiente.

2. **Configura la Aplicación como Worker.**
   - En la configuración de la aplicación, elige 'Worker' en lugar de 'Web Service'.
   - Asegúrate de que el `Procfile` esté configurado correctamente.

3. **Establece las Variables de Entorno.**
   - Configura todas las variables de entorno necesarias, como `TELEGRAM_TOKEN`.

4. **Despliega la Aplicación.**
   - Una vez configurada, procede a desplegar la aplicación.
   - Monitorea el proceso de despliegue y verifica los logs en caso de errores.

5. **Verificación.**
   - Una vez desplegado, prueba el bot en Telegram para asegurarte de que funciona como se espera.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, por favor crea un fork y envía tus cambios a través de un Pull Request.

## Licencia

Especifica aquí la licencia bajo la cual estás publicando el código (por ejemplo, MIT, GPL, etc.).
