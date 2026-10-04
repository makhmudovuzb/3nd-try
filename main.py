import telebot

TOKEN = '8862272688:AAGDkx_t1omGz6ecVHpkm04nLFj8Qre9iM0'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f"Assalomu alaykum, {user_name}! Botimizga xush kelibsiz.")

bot.polling(none_stop=True)
