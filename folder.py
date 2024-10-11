from telegram import Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler

# Функция для обработки команды /start
async def start(update: Update, context):
    # Отправляем кнопку, открывающую Web App
    await update.message.reply_text(
        "Откройте Web App!",
        reply_markup={
            "keyboard": [
                [{"text": "Открыть Web App", "web_app": WebAppInfo(url="https://alikhanamk7631.github.io/musical-guacamole/")}]
            ],
            "resize_keyboard": True,
            "one_time_keyboard": True,
        }
    )

if _name_ == "_main_":
    app = ApplicationBuilder().token('YOUR_BOT_TOKEN').build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()