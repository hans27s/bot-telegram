import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 🔐 Variables de entorno (Railway)
TOKEN = os.getenv("8663092002:AAHSltKfV9Dc4PaTsyllG5cOdWkOuAnoFqo")
CHAT_ID = os.getenv("1568924441")

tareas = {
    "Monday": ["Ir al gimnasio", "Estudiar Python"],
    "Tuesday": ["Revisar emails"],
    "Wednesday": ["Reunión"],
    "Thursday": ["Practicar código"],
    "Friday": ["Terminar pendientes"],
    "Saturday": ["Descansar"],
    "Sunday": ["Planificar semana"]
}

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if texto == "hola":
        from datetime import datetime

        hoy = datetime.now().strftime("%A")

        mensaje = f"👋 ¡Hola!\n\n📅 Hoy es {hoy}\n\n"

        if hoy in tareas:
            mensaje += "\n".join([f"✅ {t}" for t in tareas[hoy]])
        else:
            mensaje += "No tienes tareas hoy 🎉"

        await update.message.reply_text(mensaje)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot activo 🚀 Escribe HOLA")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("Bot corriendo 24/7 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()