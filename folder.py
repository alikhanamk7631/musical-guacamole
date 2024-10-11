import telebot

API_TOKEN = '7576474851:AAEWbC2mx8OrpwawkeOS94dxAkkifpEVnNE'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    web_app_url = telebot.types.WebAppInfo("https://alikhanamk7631.github.io/musical-guacamole/")  # Ссылка на твой сайт
    web_app_button = telebot.types.InlineKeyboardButton(text="Открыть Web App", web_app=web_app_url)
    keyboard.add(web_app_button)
    bot.send_message(message.chat.id, "Привет! Нажми кнопку, чтобы открыть приложение:", reply_markup=keyboard)

bot.infinity_polling()
