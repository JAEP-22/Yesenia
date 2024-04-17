import logging
import re

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Expresión regular para detectar mensajes que contienen "Hola"

expresion_regular = re.compile(r"hola", re.IGNORECASE)
expresion_menu = re.compile(r"Menu", re.IGNORECASE)
expresion_si = re.compile(r"si", re.IGNORECASE)
expresion_no = re.compile(r"No", re.IGNORECASE)
expresion_reju = re.compile(r"reju")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches the regular expression."""
    message_text = update.message.text
    if expresion_regular.search(message_text):
        await update.message.reply_text("¡Hola! Bienvenido a tu restaurante de Refresco Jurmet Favorito ¿En que te puedo ayudar?")
    elif expresion_menu.search(message_text):
        await update.message.reply_text(" El dia de hoy unicamente contamos con el menu sorpresa ¿le gustaria ordenar?")
    elif expresion_si.search(message_text):
        await update.message.reply_text(" Proporcione su direccion completa para que nuestro repartidor llegue a su casa, empezando con Calle, Colonia y numero interior")
    elif expresion_no.search(message_text):
        await update.message.reply_text("Una lastima usted se lo pierde")
    elif expresion_reju.search(message_text):
        await update.message.reply_text("Doblemente sabroso, enjoy ur meal")
    
    else:
        await update.message.reply_text("No entendí tu mensaje.")
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

def main() -> None:
    """Start the bot."""
    application = Application.builder().token("6385345516:AAE725QT22gCM0gHnxbuom9SO4NdN0UjPIw").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

   

if __name__ == "__main__":
    main()